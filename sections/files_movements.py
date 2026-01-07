from utils.utils import system_info, files_organization,folder_organization, rename_files, network_checker, files_seeker, compress_folder, backup_creation, massive_metadata_renaming
from constants import num_layout_equals
import os

def files_movements():

    while True :
        
        try:

            # ❌ Clean screen
            # ----------------

            os.system("clear")

            print("=" * num_layout_equals)
            print("⚙️  System Organization  —  Autor: Manuel Portero Leiva")
            print("=" * num_layout_equals)
            print("Selecciona una opción:")
            print("=" * num_layout_equals)
            print("💻  Opción 0: Organizar archivos por carpeta")
            print("🗂️   Opción 1: Organizador de archivos por extension")
            print("✏️   Opción 2: Renombrado masivo de archivos")
            print("🔎  Opción 3: Buscador de archivos")
            print("📦  Opción 4: Comprimir una carpeta")
            print("🌐  Opción 5: Testeador de conexión")
            print("🗂️   Opción 6: Renombrado de metadatos masivo")
            print("👋  Opcion 7: Salir")
            print("=" * num_layout_equals)

            answer = input("⚙️  Selecciona accion : ")

            match(answer):

                # 🗂️ Folder Organization
                # -----------------------

                case "0": 
                    try:
                        origin_folder = input("Introduce ruta completa de carpeta a analizar : ")
                        destination_folder = input("Introduce ruta completa de carpeta de destino : ")
                        pattern = input("Introduce el patrón de búsqueda : ")
                        folder_organization(origin_folder,destination_folder,pattern)
                    except Exception as e:
                        print(f"❌ Error al realizar la accion : {e}")

                # 🗂️ Files Organization
                # -----------------------

                case "1":
                    try:
                        folder = input("Introduce ruta completa de carpeta : ")
                        files_organization(folder)
                    except Exception as e:
                        print(f"❌ Error al realizar la accion : {e}")

                # ✏️  Files massive renaming
                # ---------------------------

                case "2":
                    try:
                        folder = input("Introduce ruta completa de carpeta : ")
                        header = input("Introduce prefijo : ")
                        rename_files(folder,header)
                    except Exception as e:
                        print(f"❌ Error al realizar la accion : {e}")

                # 🔎  Files Search
                # -----------------------

                case "3":
                    try:
                        folder = input("Introduce ruta completa de carpeta : ")
                        pattern = input("Introduce el patrón de búsqueda : ")
                        files_seeker(folder,pattern)
                    except Exception as e:
                        print(f"❌ Error al realizar la accion : {e}")

                # 📦 Compress files
                # -----------------------    

                case "4":
                    try:
                        folder = input("Introduce ruta completa de carpeta a comprimir: ")
                        file = input("Introduce el nombre del archivo a comprimir: ")
                        compress_folder(folder,file)
                    except Exception as e:
                        print(f"❌ Error al realizar la accion : {e}")
                # 🌐 Network test
                # -----------------------    

                case "5":
                    try:
                        network_checker()
                    except Exception as e:
                        print(f"❌ Error al realizar la accion : {e}")
                
                # 🗂️ Renombrado massivo de metadatos
                # --------------------------------
                case "6":
            
                    while True : 
                        try:
                            folder_path = input("Por favor introduce la ruta del directorio : ")
                            album = input("Por favor introduce el album : ")
                            style = input("Por favor introduzca el estilo : ")
                            artist = input("Por favor introduzca el artista : ")
                            massive_metadata_renaming(folder_path,album,artist,style)

                        except Exception as e:
                            print(f"❌ Error al realizar la accion : {e}")

                        exit_answer = input("Deseas salir del programa de renombrado de carpetas? (Yes/No) :")
             
                        if exit_answer.lower() == "yes" :                
                            print("❌ Saliendo del subprograma ...")
                            break

                # 👋 Exit
                # -----------------------    

                case "7":
                
                    print("👋 Saliendo de la consola de movimiento de archivos.")
                    break            

            # 👋 Exit dialog
            # -----------------------    

            break_option = input("¿Deseas salir del subprograma de organización de archivos? (Yes/No): ")
            
            if break_option.lower() == "y" or break_option.lower() == "yes" :
                break
                break # the first break, breaks the match case , the second break the while
                
        
        except Exception as e:
            print(f"❌ Error de seleccion: {e}")    