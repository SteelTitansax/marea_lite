from contextlib import contextmanager
import sys
import os
import sqlite3
from constants import DB_PATH
import requests
import platform
from pathlib import Path
import shutil
import time
import zipfile
import subprocess
import requests
from tqdm import tqdm

# System Info 
# --------------------

def system_info():
    print(f"Sistema: {platform.system()}")
    print(f"Versión: {platform.release()}")
    print(f"Arquitectura: {platform.machine()}")
    print(f"Directorio actual: {os.getcwd()}")
    print(f"Espacio libre: {os.statvfs('/').f_bfree * os.statvfs('/').f_bsize / (1024**3):.2f} GB")

# Wikipedia Search
# --------------------------

def wikipedia_search(query):
    try:
        url = "https://es.wikipedia.org/api/rest_v1/page/summary/" + query.replace(" ", "_")
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if 'extract' in data:
                return data['extract']
            else:
                return "No se encontró un resumen para esa consulta."
        else:
            return "No se encontró información en Wikipedia."
    except Exception as e:
        return f"Error accediendo a Wikipedia: {e}"


# Silent Warning
# ------------------------

@contextmanager
def suppress_output():
    with open(os.devnull, "w") as devnull:
        old_stdout = sys.stdout
        old_stderr = sys.stderr
        try:
            sys.stdout = devnull
            sys.stderr = devnull
            yield
        finally:
            sys.stdout = old_stdout
            sys.stderr = old_stderr

# Files organization
# ------------------------

def files_organization(folder):
    extensions = {
        'imagenes': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
        'documentos': ['.pdf', '.doc', '.docx', '.txt', '.xlsx'],
        'videos': ['.mp4', '.avi', '.mkv', '.mov'],
        'musica': ['.mp3', '.wav', '.flac']
    }
    
    for file in os.listdir(folder):
        if os.path.isfile(os.path.join(folder, file)):
            ext = os.path.splitext(file)[1].lower()
            
            for category, exts in extensions.items():
                if ext in exts:
                    destination_folder = os.path.join(folder, category)
                    os.makedirs(destination_folder, exist_ok=True)
                    shutil.move(
                        os.path.join(folder, file),
                        os.path.join(destination_folder, file)
                    )
                    print(f"Movido: {file} -> {category}")
                    break
    
    print("Archivos organizados")


# Files renaming
# ------------------------

def rename_files(folder, header):
    counter = 1
    for file in os.listdir(folder):
        old_path = os.path.join(folder, file)
        if os.path.isfile(old_path):
            nombre, extension = os.path.splitext(file)
            nuevo_nombre = f"{header}_{counter:03d}{extension}"
            new_path = os.path.join(folder, nuevo_nombre)
            
            os.rename(old_path, new_path)
            print(f"Renombrado: {file} -> {nuevo_nombre}")
            counter += 1   
            

# Network checker functions
# ---------------------------

def network_checker(urls=["https://google.com", "https://github.com"]):
    for url in urls:
        try:
            start = time.time()
            answer = requests.get(url, timeout=5)
            time_watch = time.time() - start
            print(f"✅ {url} - {answer.status_code} - {time_watch:.2f}s")
        except:
            print(f"❌ {url} - Sin conexión")

# Folder organization
# ------------------------

def folder_organization(origin_folder, destination_folder, pattern):
    results = []
    
    # Create destination folder if no exists
    os.makedirs(destination_folder, exist_ok=True)
    
    for root, folders, files in os.walk(origin_folder):
        for file in files:
            if pattern.lower() in file.lower():
                full_path = os.path.join(root, file)
                results.append(full_path)
                print(f"Encontrado: {full_path}")
                
                # Build destination route
                destination_file_path = os.path.join(destination_folder, file)
                
                try:
                    shutil.move(full_path, destination_file_path)
                    print(f"Movido: {file} -> {os.path.basename(destination_file_path)}")
                except Exception as e:
                    print(f"❌ Error moviendo {file}: {e}")
    
    return results



# Files seeker functions
# ------------------------

def files_seeker(folder, pattern):
    results = []
    for root, folders, files in os.walk(folder):
        for files in files:
            if pattern.lower() in files.lower():
                full_path = os.path.join(root, files)
                results.append(full_path)
                print(f"Encontrado: {full_path}")
    return results


# Folder compression function
# -----------------------------

def compress_folder(folder, zip_file):
    with zipfile.ZipFile(zip_file, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, folders, files in os.walk(folder):
            for file in files:
                full_path = os.path.join(root, file)
                file_name = os.path.relpath(full_path, folder)
                zipf.write(full_path, file_name)
                print(f"Comprimido: {file_name}")


# Youtube downloader function
# -----------------------------

def youtube_video_downloader(output_dir):
    
    while True :
        
        try:

            youtubeUrl = input("Por favor introduzca url de lista o video a descargar: ")
            fileFormat = input("Introduzca el formato del archivo (validos mp3 o mp4): ")
            new_folder_answer = input("Deseas crear una nueva carpeta (Yes/No)?")

            if new_folder_answer.lower() == "yes" or new_folder_answer.lower() == "y":
               new_folder = input("Introduce el nombre de la carpeta")
               new_folder_path = output_dir / new_folder
               new_folder_path.mkdir(parents=True, exist_ok=True)
               print(f"Carpeta creada: {new_folder_path}")
               output_dir = new_folder_path

            if fileFormat == "mp3":

    
                subprocess.run(
                ["yt-dlp", "-x", "--audio-format", "mp3", youtubeUrl],
                cwd=output_dir
                )
                break

            elif fileFormat == "mp4":

                subprocess.run(
                ["yt-dlp", "-t", "mp4", youtubeUrl],
                cwd=output_dir
                )
                break
            else:
                print("Introduce un formato de archivo valido")
        except Exception as e:
            print(f"❌ Error de seleccion: {e}")    


# Create backup function 
# ------------------------

def backup_creation(drive_name, username, verbose,one_folder_name, one_folder=False):
    """
        Copy files from one folder to another , updating only if the modified date of destiny is less than origin

        Args: 
            drive_name: name of the backup external drive
            username: name of laptop user
            verbose: verbose mode 
    """
    destination_path_array = [f"/media/{username}/{drive_name}/Documentos",f"/media/{username}/{drive_name}/Imágenes",f"/media/{username}/{drive_name}/Música",f"/media/{username}/{drive_name}/Biblioteca"]

    origin_path_array = [f"/home/{username}/Documentos",f"/home/{username}/Imágenes",f"/home/{username}/Música",f"/home/{username}/Biblioteca"]
    
    if one_folder :
        destination_path_array = [f"/media/{username}/{drive_name}/{one_folder_name}"]
        origin_path_array =  [f"/home/{username}/{one_folder_name}"]

    loop_range = enumerate(origin_path_array)
    
    for loop_position , loop_path in loop_range :
        
        origin_path = Path(origin_path_array[loop_position])
        destination_path = Path(destination_path_array[loop_position])
        
        print( f"Creando backup de {origin_path} ...")
        # Build cp command

        command_subprocess = ["rsync", "-aun", "--out-format=%n", f"{origin_path}/", f"{destination_path}/"]
        
        print(f"Ejecutando: {' '.join(command_subprocess)}")
        
        try:
            if verbose: 
                result = subprocess.run(
                    command_subprocess,
                    capture_output=True, text=True, check=True
                )
            else:
                result = subprocess.run(command_subprocess)

            files_to_copy = [f for f in result.stdout.splitlines() if f]
        
            total_files = len(files_to_copy)

            if total_files == 0:
                print("✅ Todo está actualizado. No hay archivos nuevos.")
                continue

            # Paso 2: ejecutar rsync y mostrar barra de progreso
            print(f"Archivos a copiar/actualizar: {total_files}")

            with tqdm(total=total_files, desc="Copiando", unit="archivo", ncols=80) as pbar:
                for file in files_to_copy:
                    src = origin_path / file
                    dst = destination_path / file
                    dst.parent.mkdir(parents=True, exist_ok=True)
                    try:
                        subprocess.run(["cp", "-pu", str(dst), str(src)], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                    except Exception:
                        pass
                    pbar.update(1)

            if result.returncode == 0:
                print(f"✅ Completado el backup de {origin_path}")
                if verbose and result.stdout:
                    print("Salida:")
                    print(result.stdout)
            else:
                print(f"❌ Error en backup de {origin_path}")
                if result.stderr:
                    print("Error:")
                    print(result.stderr)
                    
        except Exception as e:
            print(f"❌ Excepción al ejecutar backup: {e}")
    
    print(f"Proceso de backup {origin_path} finalizado")

# Restore backup function 
# ------------------------

def restore_backup(drive_name, username, verbose,one_folder_name, one_folder=False):
    """
        Copy files from one folder to another , updating only if the modified date of destiny is less than origin

        Args: 
            drive_name: name of the backup external drive
            username: name of laptop user
            verbose: verbose mode 
    """

    origin_path_array = [f"/home/{username}/Documentos",f"/home/{username}/Imágenes",f"/home/{username}/Música",f"/home/{username}/Biblioteca"]
    destination_path_array = [f"/media/{username}/{drive_name}/Documentos",f"/media/{username}/{drive_name}/Imágenes",f"/media/{username}/{drive_name}/Música",f"/media/{username}/{drive_name}/Biblioteca"]
    
    if one_folder :
        origin_path_array = [f"/home/{username}/{one_folder_name}"]
        destination_path_array = [f"/media/{username}/{drive_name}/{one_folder_name}"]

    loop_range = enumerate(origin_path_array)
    
    for loop_position , loop_path in loop_range :
        
        origin_path = Path(origin_path_array[loop_position])
        destination_path = Path(destination_path_array[loop_position])
        
        print( f"Creando backup de {origin_path} ...")
        # Build cp command

        command_subprocess = ["rsync", "-aun", "--out-format=%n", f"{origin_path}/", f"{destination_path}/"]
        
        print(f"Ejecutando: {' '.join(command_subprocess)}")
        
        try:
            if verbose: 
                result = subprocess.run(
                    command_subprocess,
                    capture_output=True, text=True, check=True
                )
            else:
                result = subprocess.run(command_subprocess)

            files_to_copy = [f for f in result.stdout.splitlines() if f]
        
            total_files = len(files_to_copy)

            if total_files == 0:
                print("✅ Todo está actualizado. No hay archivos nuevos.")
                continue

            # Paso 2: ejecutar rsync y mostrar barra de progreso
            print(f"Archivos a copiar/actualizar: {total_files}")

            with tqdm(total=total_files, desc="Copiando", unit="archivo", ncols=80) as pbar:
                for file in files_to_copy:
                    src = origin_path / file
                    dst = destination_path / file
                    dst.parent.mkdir(parents=True, exist_ok=True)
                    try:
                        subprocess.run(["cp", "-pu", str(dst), str(src)], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                    except Exception:
                        pass
                    pbar.update(1)

            if result.returncode == 0:
                print(f"✅ Completado el backup de {origin_path}")
                if verbose and result.stdout:
                    print("Salida:")
                    print(result.stdout)
            else:
                print(f"❌ Error en backup de {origin_path}")
                if result.stderr:
                    print("Error:")
                    print(result.stderr)
                    
        except Exception as e:
            print(f"❌ Excepción al ejecutar backup: {e}")
    
    print(f"Proceso de retablecimiento de backup {origin_path} finalizado")

def create_iso(output_path,iso_name,iso_volume_name, input_path):
    try:
        subprocess.run(["mkisofs", "-o", f"{output_path}/{iso_name}" , "-V", iso_volume_name,"-J","-R",input_path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except Exception as e:
        print(f"Error durante la accion {e}")



def massive_metadata_renaming(folder_path,album,artist,style):

    for file in os.listdir(folder_path):
        
        full_path = f"{folder_path}/{file}" 
        print(f"Changing {file} metadata...")

        # Temporary file
        # --------------

        new_file = os.path.join(folder_path, f"m-{file}")

        # Build FFmpeg command
        # --------------------
        
        cmd = [
            'ffmpeg',
            '-i', full_path,
            '-c', 'copy',
            '-metadata', f"title={os.path.splitext(file)[0]}",
            '-metadata', f"album={album}",
            '-metadata', f"artist={artist}",
            '-metadata', f"genre={style}",
            new_file
        ]
        
        try:

            # Run FFmpeg
            result = subprocess.run(
                cmd,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
 
            if str(result.returncode) == "0":
                # Replace original file for temporary file
                os.remove(full_path)
                print(f"✓ Metadatos actualizados: {full_path}")
            else:
                print(f"✗ Error en ffmpeg: {result.stderr}")
                if os.path.exists(new_file):
                    os.remove(new_file)

        except subprocess.CalledProcessError as e:
            print(f"✗ Error procesando {file}: {e.stderr}")
            # Clean temporary file if exists
            if os.path.exists(new_file):
                os.remove(new_file)
            return False


    return True
