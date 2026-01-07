# Multimedia conversor 
# ----------------------------------------------------------------------------------------------------------------------
# Purpose : Exchange multimedia format using AI ( Text to Audio, Image to text, Text to language text ) and interact
# as an interface in between Linux OS and Android or other OS devices via browser
# ----------------------------------------------------------------------------------------------------------------------
# Author : Manuel Portero Leiva 
# ----------------------------------------------------------------------------------------------------------------------

import os
from constants import INPUT_DIR, OUTPUT_DIR,num_layout_equals, QB_URL, QB_PASSWORD, QB_USER
from server.chatbot_http_server import chatbot_http_server
from utils.multimedia_utis import *
from utils.utils import youtube_video_downloader
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(INPUT_DIR, exist_ok=True)


def multimedia_conversor():
    while True:

        try:

            clear_console()
            print("=" * num_layout_equals)
            print("🧰 Multimedia Conversor - Autor Manuel Portero")
            print("=" * num_layout_equals)
            menu_items = [
                ("📂", "1", "Archivo a texto (PDF, DOCX, EPUB, TXT)"),
                ("🖼️", " 2", "  Imagen a texto (OCR)"),
                ("🔊", "3", "Texto a audio (TTS multilenguaje)"),
                ("🌐", "4", "Traducir texto desde archivo"),
                ("🖥️", " 5", "  Iniciar servidor HTTP para transferencia de archivos PDA"),
                ("🎵", "6", "Descargador de audio de YouTube"),
                ("🖥️", " 7", "  Descargar torrent"),
                ("📂", "8", "Mover archivos de 'pda_output' a 'pda_input'"),
                ("📂", "9", "Mover archivos de 'pda_input' a 'pda_output'"),
                ("🗑️", " 10", "  Borrar todos los archivos de 'pda_input'"),
                ("🗑️", " 11", "  Borrar todos los archivos de 'pda_output'"),
                ("❌", "12", "Salir")
            ]

            for icon, number, description in menu_items:
                # We impose this loop for align the icons properly
                print(f"{icon} {number}".ljust(6) + description)
            print("=" * num_layout_equals)
            
            answer = input("\n👉  Selecciona una opción: ")

            match(answer):

                case "1":
                    while True:
                        try:
                            filename = input("📂 Nombre del archivo (PDF/DOCX/EPUB/TXT) en 'input/': ")
                            path = INPUT_DIR / filename
                            if not path.exists():
                                print("❌ Archivo no encontrado en la carpeta 'input'.")
                                
                                continue
                            text = file_to_text(str(path))
                            print("\n 👉 TEXTO EXTRAÍDO:\n")
                            print(text[:1000] + "\n...")

                            word_count = len(text.split())
                            if word_count > 20000:
                                print(f"👉 El texto tiene {word_count} palabras, se dividirá en volúmenes de 20000 palabras.")
                                save_text_in_volumes(text, filename, max_words=20000)
                            else:
                                save_text(text, filename)

                        except Exception as e:
                                print(f"Error: {e}")
                    
                        exit_question = input ("Deseas salir de la acción y no procesar mas archivos ? (Yes/No)")
                        if exit_question.lower() == "y" or exit_question.lower() == "yes" :
                            break
                                

                case "2":
                    while True:
                        try:
                            filename = input("📂 Nombre de la imagen (JPG/PNG) en 'input/': ")
                            path = INPUT_DIR / filename
                            if not path.exists():
                                print("❌ Imagen no encontrada en 'input'.")
                                continue
                            text = image_to_text(str(path))
                            print("\n📂 TEXTO OCR:\n")
                            print(text)
                            save_text(text, f"{filename.split('.')[0]}.txt")

                            
                        except Exception as e:
                                print(f"Error: {e}")
                        
                        exit_question = input ("Deseas salir de la acción y no procesar mas archivos ? (Yes/No): ")

                        if exit_question.lower() == "y" or exit_question.lower() == "yes" :
                            break

                case "3":
                    while True:
                        try:

                            text_input = input("📂 Texto a convertir a voz: ")
                            text_output = input("👉 Nombre del archivo de audio (output.mp3): ") or "output.mp3"
                            lang = input("Idioma (ej: es, en, fr, de): ") or "es"
                            print(f"👉 Procesando {text_input}. Dividiendo en volumenes ... ")

                            text_to_audio_in_volumes(text_input, text_output, lang, max_words=5000)
                        
                        except Exception as e:
                                print(f"Error: {e}")
                        
                        exit_question = input ("Deseas salir de la acción y no procesar mas archivos ? (Yes/No)")

                        if exit_question.lower() == "y" or exit_question.lower() == "yes" :
                            break    
                case "4":
                    while True:
                        try:
                            filename = input("📂 Nombre del archivo de texto en 'input/': ")
                            path = INPUT_DIR / filename
                            lang = input("Idioma destino (ej: en, es, fr): ")
                            if not path.exists():
                                print("❌  Archivo no encontrado en 'input'.")
                                continue

                            try:

                                text = path.read_text(encoding='utf-8')
                                
                                if text:
                                    print("Iniciando traduccion online...")
                                    translated = translate_text_in_chunks_online(text, lang)
                                    print(f"\n 📂 TEXTO TRADUCIDO [{lang}]:\n{translated[:1000]}...\n")
                                    save_text(translated, f"{filename.split('.')[0]}_translated_{lang}.txt")
                                
                                else:
                                    print("❌ El archivo está vacío.")
                            
                            except Exception as e:
                                print(f"❌ Ocurrió un error: {e}")

                        except Exception as e:
                                print(f"Error: {e}")
                        
                        exit_question = input ("Deseas salir de la acción y no procesar mas archivos ? (Yes/No)")
                        if exit_question.lower() == "y" or exit_question.lower() == "yes" :
                            break
    
                case "5":
                    try:
                        print("🖥️ Iniciando servidor Flask en http://0.0.0.0:8080 ... (CTRL+C para detener)")
                        chatbot_http_server()
                    except Exception as e:
                        print(f"❌ Error al realizar la accion : {e}")

                case "6":
                    try:
                        while True : 
                            youtube_video_downloader(OUTPUT_DIR)
                        
                            exit_question = input ("Deseas salir de la acción y no descargar mas archivos ? (Yes/No)")

                            if exit_question.lower() == "y" or exit_question.lower() == "yes" :
                                break
                    except Exception as e:
                        print(f"❌ Error al realizar la accion : {e}")

                case "7":
                    try:
                        while True :
                            download_torrent(QB_USER,QB_PASSWORD,QB_URL)
                            exit_question = input ("Deseas salir de la acción y no descargar mas archivos ? (Yes/No)")

                            if exit_question.lower() == "y" or exit_question.lower() == "yes" :
                                break
                    except Exception as e:
                        print(f"❌ Error al realizar la accion : {e}")

                case "8":
                    try:
                        move_files(OUTPUT_DIR, INPUT_DIR)
                    except Exception as e:
                        print(f"❌ Error al realizar la accion : {e}")

                case "9":
                    try:
                        move_files(INPUT_DIR, OUTPUT_DIR)
                    except Exception as e:
                        print(f"❌ Error al realizar la accion : {e}")

                case "10":
                    try:
                        clear_directory(INPUT_DIR)
                    except Exception as e:
                        print(f"❌ Error al realizar la accion : {e}")

                case "11":
                    try:
                        clear_directory(OUTPUT_DIR)
                    except Exception as e:
                        print(f"❌ Error al realizar la accion : {e}")

                case "12":
                    print("👋 Saliendo de PDA Menu.")
                    break
                    break

                case _:
                    print("❌ Opción inválida.")

        except Exception as e:
            print(f"❌ Error de seleccion: {e}")    
