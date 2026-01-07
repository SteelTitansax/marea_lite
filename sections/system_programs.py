from utils.utils import system_info, files_organization, rename_files, network_checker, files_seeker, compress_folder, backup_creation, massive_metadata_renaming
from constants import num_layout_equals
import os

def system_organization():

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
            print("💻  Opción 1: Información del sistema")
            print("🗂️   Opción 2: Organizar archivos")
            print("✏️   Opción 3: Renombrado masivo de archivos")
            print("🔎  Opción 4: Buscador de archivos")
            print("📦  Opción 5: Comprimir una carpeta")
            print("🌐  Opción 6: Testeador de conexión")
            print("💻  Opción 7: Crear backup")
            print("🗂️   Opción 8: Renombrado de metadatos masivo")
            print("👋  Opcion 9: Salir")
            print("=" * num_layout_equals)

            answer = input("⚙️  Selecciona accion : ")

            match(answer):

                # 💻 System Information
                # -----------------------

                case "1": 
                    try:
                        system_info()
                    except Exception as e:
                        print(f"❌ Error al iniciar el servidor Flask: {e}")

                # 🗂️ Files Organization
                # -----------------------

                case "2":
                    try:
                        folder = input("Introduce ruta completa de carpeta : ")
                        files_organization(folder)
                    except Exception as e:
                        print(f"❌ Error al iniciar el servidor Flask: {e}")

                # ✏️  Files massive renaming
                # ---------------------------

                case "3":
                    try:
                        folder = input("Introduce ruta completa de carpeta : ")
                        header = input("Introduce prefijo : ")
                        rename_files(folder,header)
                    except Exception as e:
                        print(f"❌ Error al iniciar el servidor Flask: {e}")

                # 🔎  Files Search
                # -----------------------

                case "4":
                    try:
                        folder = input("Introduce ruta completa de carpeta : ")
                        pattern = input("Introduce el patrón de búsqueda : ")
                        files_seeker(folder,pattern)
                    except Exception as e:
                        print(f"❌ Error al iniciar el servidor Flask: {e}")

                # 📦 Compress files
                # -----------------------    

                case "5":
                    try:
                        folder = input("Introduce ruta completa de carpeta a comprimir: ")
                        file = input("Introduce el nombre del archivo a comprimir: ")
                        compress_folder(folder,file)
                    except Exception as e:
                        print(f"❌ Error al iniciar el servidor Flask: {e}")
                # 🌐 Network test
                # -----------------------    

                case "6":
                    try:
                        network_checker()
                    except Exception as e:
                        print(f"❌ Error al iniciar el servidor Flask: {e}")

                # 💻 Backup creation
                # -----------------------

                case "7":
                    try:
                        drive_name = input("Por favor introduce el nombre del external drive : ")
                        username = input("Por favor introduce el username de la computadora : ")
                        verbose_input = input("Quieres correr el backup en modo verbose?(Yes/No) : ")
                    
                        if verbose_input.lower() == "yes":
                            verbose = True
                        else:
                            verbose = False                
                
                        backup_creation(drive_name, username, verbose)
                    except Exception as e:
                        print(f"❌ Error al iniciar el servidor Flask: {e}")
                
                # 🗂️ Renombrado massivo de metadatos
                # --------------------------------
                case "8":
            
                    while True : 
                        try:
                            folder_path = input("Por favor introduce la ruta del directorio : ")
                            album = input("Por favor introduce el album : ")
                            style = input("Por favor introduzca el estilo : ")
                            artist = input("Por favor introduzca el artista : ")
                            massive_metadata_renaming(folder_path,album,artist,style)

                        except Exception as e:
                            print(f"❌ Error al iniciar el servidor Flask: {e}")

                        exit_answer = input("Deseas salir del programa de renombrado de carpetas? (Yes/No) :")
             
                        if exit_answer.lower() == "yes" :                
                            print("❌ Saliendo del subprograma ...")
                            break

                # 👋 Exit
                # -----------------------    

                case "9":
                
                    print("👋 Saliendo de la system organization console.")
                    break            

            # 👋 Exit dialog
            # -----------------------    

            break_option = input("¿Deseas salir del subprograma de organización de archivos? (Yes/No): ")
            
            if break_option.lower() == "y" or break_option.lower() == "yes" :
                break
                break # the first break, breaks the match case , the second break the while
                
        
        except Exception as e:
            print(f"❌ Error de seleccion: {e}")    