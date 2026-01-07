import os
import requests
import subprocess
import shutil
import asyncio
import edge_tts
import pytesseract
import textwrap
import warnings
from docx import Document
from pathlib import Path
from pdf2image import convert_from_path
from utils.utils import suppress_output
from PIL import Image
from ebooklib import epub, ITEM_DOCUMENT
from constants import INPUT_DIR, OUTPUT_DIR
from bs4 import BeautifulSoup
from pydub import AudioSegment
from TTS.utils.radam import RAdam
from TTS.api import TTS
from pydub import AudioSegment
from deep_translator import GoogleTranslator

os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(INPUT_DIR, exist_ok=True)

def clear_console():
    os.system('clear' if os.name == 'posix' else 'cls')

def pdf_to_text(path):
    images = convert_from_path(path)
    text = ''
    for i, image in enumerate(images):
        temp = OUTPUT_DIR / f"page_{i}.png"
        image.save(temp, 'PNG')
        text += pytesseract.image_to_string(Image.open(temp)) + "\n"
    return text

def docx_to_text(filepath):
    doc = Document(filepath)
    return "\n".join([p.text for p in doc.paragraphs])

def epub_to_text(path):
    text = ""
    book = epub.read_epub(path)
    for item in book.get_items():
        if item.get_type() == ITEM_DOCUMENT:
            soup = BeautifulSoup(item.get_content(), 'html.parser')
            text += soup.get_text() + "\n"
    return text

def file_to_text(path):
    if path.endswith(".pdf"):
        return pdf_to_text(path)
    elif path.endswith(".docx"):
        return docx_to_text(path)
    elif path.endswith(".epub"):
        return epub_to_text(path)
    else:
        return image_to_text(path)

def image_to_text(path):
    return pytesseract.image_to_string(Image.open(path))

def get_next_part(base_name):
    i = 1
    while os.path.exists(f"{base_name}_part_{i}.mp3"):
        i += 1
    return i

# We consider local devices too with coquiTTS model, for better quality we use EdgeTTS
# -------------------------------------------------------------------------------------

def text_to_audio_in_volumes(text_input, text_output="output.mp3", lang="es", max_words=5000, bool_local=False):
    input_path = INPUT_DIR / text_input
    
    with open(input_path, "r", encoding="utf-8") as f:
        text = f.read()

    chunks = textwrap.wrap(text, 4000)
    
    output_base = str(input_path).replace(".txt", "")
    next_part = get_next_part(output_base)

    generated_files = []


    if bool_local:
        
        model_map_coqui = {
            "es": "tts_models/es/css10/vits",
            "en": "tts_models/en/ljspeech",
            "fr": "tts_models/fr/css10",
            "de": "tts_models/de/thorsten",
            "it": "tts_models/it/mai_female",
            "pt": "tts_models/pt/cv_female"
        }

        print("🔊 Usando Coqui TTS (local/offline)...")
        warnings.filterwarnings("ignore")
        with suppress_output():        
            model_name = model_map_coqui.get(lang, "tts_models/urd-script_devanagari/fairseq/vits")
            tts = TTS("tts_models/es/css10/vits", progress_bar=False, gpu=False)
    else:
        
        voice_map_edge = {
            "es": "es-ES-ElviraNeural",
            "en": "en-US-AriaNeural",
            "fr": "fr-FR-DeniseNeural",
            "de": "de-DE-KatjaNeural",
            "it": "it-IT-ElsaNeural",
            "pt": "pt-BR-FranciscaNeural"
        }
        print("🔊 Usando Edge TTS (online)...")
        voice = voice_map_edge.get(lang, "es-ES-ElviraNeural")

    async def generate_audio_edge(text, output_file):
        communicate = edge_tts.Communicate(text, voice=voice)
        await communicate.save(output_file)

    for i, chunk in enumerate(chunks):
        output_file = f"{output_base}_part_{next_part + i}.mp3"
        if bool_local:
            with suppress_output():        
                tts.tts_to_file(text=str(chunk), file_path=output_file)
        else:
            asyncio.run(generate_audio_edge(str(chunk), output_file))
        generated_files.append(output_file)
        print(f"== Audio guardado: {output_file} ==")

    # Consolidar audios
    # ------------------
    consolidated_audio = AudioSegment.empty()
    for mp3_file in generated_files:
        consolidated_audio += AudioSegment.from_mp3(mp3_file)

    output_path = OUTPUT_DIR / text_output
    consolidated_audio.export(output_path, format="mp3")
    print(f"=== Audio consolidado guardado en: {output_path} ===")

    # Limpiar temporales
    for mp3_file in generated_files:
        os.remove(mp3_file)
        print(f"Archivo temporal eliminado: {mp3_file}")

    os.remove(INPUT_DIR / text_input)
    print(f"Archivo de texto eliminado: {text_input}")

# Translate text functions
# ---------------------------

def translate_text(text, target='en'):
    return GoogleTranslator(source='auto', target=target).translate(text)
    
def translate_text_in_chunks_online(text, target='en', chunk_size=4500,source_lang='auto'):
    chunks = textwrap.wrap(text, chunk_size)
    translated_chunks = []
    temp_files = []

    for i, chunk in enumerate(chunks):
        print(f"Traduciendo chunk {i+1} de {len(chunks)}...")
        translated_chunk = translate_text(chunk, target)
        temp_file_path = OUTPUT_DIR / f"translated_chunk_{i+1}.txt"
        temp_file_path.write_text(translated_chunk, encoding='utf-8')
        temp_files.append(temp_file_path)

    final_text = ""
    for temp_path in temp_files:
        final_text += temp_path.read_text(encoding='utf-8') + "\n"
        temp_path.unlink()  # Delete temporal chunk

    return final_text

def save_text_in_volumes(text, base_name, max_words=20000):
    words = text.split()
    total_words = len(words)
    volumes = (total_words // max_words) + (1 if total_words % max_words > 0 else 0)

    for i in range(volumes):
        start = i * max_words
        end = start + max_words
        volume_words = words[start:end]
        volume_text = " ".join(volume_words)
        volume_name = f"{Path(base_name).stem}_volume_{i+1}.txt"
        path = INPUT_DIR / volume_name
        path.write_text(volume_text, encoding='utf-8')
        print(f"=== Texto guardado en: {path} ===")

def save_text(text, name):
    output_name = Path(name).stem + ".txt"
    path = INPUT_DIR / output_name
    path.write_text(text, encoding='utf-8')
    print(f"=== Texto guardado en: {path} ===")

def move_files(src_dir, dest_dir):
    for file_path in src_dir.iterdir():
        if file_path.is_file():
            shutil.move(str(file_path), dest_dir / file_path.name)
    print(f"📂 Archivos movidos de {src_dir} a {dest_dir}")

def clear_directory(directory):
    for file_path in directory.iterdir():
        if file_path.is_file():
            file_path.unlink()
    print(f"=== Todos los archivos de {directory} han sido eliminados. ===")

# Download torrent functions
# ---------------------------

def download_torrent(QB_USER,QB_PASSWORD,QB_URL) :
    session = requests.Session()

    # Get terminal wide range

    terminal_width = os.get_terminal_size().columns
    separator = "=" * terminal_width

    # Header
    print(separator)
    print("Torrent Searcher Tool".center(terminal_width))
    print(separator)
    print()

    # Input keyword

    search_name = input("Introduce el la palabra de busqueda del torrent: ")
    print()
    print(separator)
    print()
    search_url = f"https://thpibay.xyz/search/{search_name}/1/99/0"

    response = requests.get(search_url)

    soup = BeautifulSoup(response.content, 'html.parser')

    search_results = soup.select_one('table#searchResult')

    torrents_selection = []

    # Getting all torrents information

    if search_results:
    
        rows = search_results.select('tr')
            
        counter=0
       

        for i,row in enumerate(rows,start=1):
    
            title_tag = row.select_one('a.detLink')
            magnet_tag = row.select_one('a[href^="magnet:"]')
    
            if title_tag and magnet_tag :
                title = title_tag.text.strip()
                magnet = magnet_tag['href']

                torrents_selection.append({
                    "id": counter,
                    "title": title,
                    "magnet": magnet
                })

                print(f"Id: {counter} - {title}")
                counter = counter + 1

        print()
        print(separator)
        print()
        
        if len(torrents_selection) > 0:
           selection_input = input("Please select the input to donwload (Input the id of the list): ")
           torrent_id = int(selection_input)
           torrent_selected_magnet = torrents_selection[torrent_id]['magnet']
            
           torrent_type = input("Do you want to add the torrent via qbittorrent (otherwise transmission) (Yes/No)")

           if torrent_type.lower() == "yes" or torrent_type.lower() == "y": 
               # Login
               login_resp = session.post(
                   f"{QB_URL}/api/v2/auth/login",
                   data={"username": QB_USER, "password": QB_PASSWORD}
               )

               if login_resp.text != "Ok.":
                  print("Error al iniciar sesión en qBittorrent Web")
                  exit()

               # Añadir torrent
               add_resp = session.post(
                 f"{QB_URL}/api/v2/torrents/add",
                 data={"urls": torrent_selected_magnet}
               )

               if add_resp.status_code == 200:
                  print("Torrent agregado correctamente a qBittorrent Web")
               else:
                  print(f"Error al agregar torrent: {add_resp.status_code} - {add_resp.text}")
            
           else:

             # Adding the torrent to Transmission/qbittorrent
             subprocess.Popen(['xdg-open',torrent_selected_magnet],
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE)
             print()
             print(separator)
             print()
             print(f"{title} torrent added successfully.")

        else:
            print("No torrents found")

    else:
        print("No search result found.")