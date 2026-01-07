from utils.utils import backup_creation,create_iso
from constants import num_layout_equals,personal_computer_installation_packages,laptop_installation_packages,phone_installation_packages,tablet_installation_packages
import os

def backup_flash_isos():

    while True :
        
        try:

            # ❌ Clean screen
            # ----------------

            os.system("clear")

            print("=" * num_layout_equals)
            print("⚙️  Backup / Flash / Iso  —  Autor: Manuel Portero Leiva")
            print("=" * num_layout_equals)
            print("Selecciona una opción:")
            print("=" * num_layout_equals)
            print("🖥️    Opción 0: Crear backup")
            print("💻   Opción 1: Crear ISO")
            print("❌   Opción 2: Salir")
            print("=" * num_layout_equals)

            answer = input("⚙️  Selecciona acción: ")

            match(answer):

                # 💻 Backup creation
                # ---------------------------------------------

                case "0": 
                    try:
                        
                        print("=== Creando Backup ===")  

                        drive_name = input("Por favor introduce el nombre del external drive : ")
                        username = input("Por favor introduce el username de la computadora : ")
                        one_folder = input("Quieres el backup usual o solo una carpeta (Yes/No)?")
                        if one_folder.lower() == "y" or one_folder.lower() == "yes" :
                            one_folder_name = input("Introduce el nombre de la carpeta : ")
                            one_folder = True
                        else:
                            one_folder_name = ""
                            one_folder = False
                        verbose_input = input("Quieres correr el backup en modo verbose?(Yes/No) : ")
                    
                        if verbose_input.lower() == "yes":
                            verbose = True
                        else:
                            verbose = False                
                
                        backup_creation(drive_name, username, verbose, one_folder_name, one_folder=one_folder)
                    except Exception as e:
                        print(f"❌ Error al realizar la accion : {e}")
                
                # 💻 ISO creation 
                # --------------------------

                case "1":
                    try:

                        print("=== Grabar imagen en USB desde ISO ===")  
                        output_path = input("Por favor introduce la ruta de salida del archivo ISO : ")
                        input_path = input("Por favor introduce la ruta de entrada del archivo ISO : ")
                        iso_name = input("Por favor introduce el nombre del archivo ISO : ")
                        iso_volume_name = input("Por favor introduce el nombre del volumen del archivo ISO : ")
                        create_iso(output_path,iso_name,iso_volume_name, input_path)
                        print(f"✅ {iso_name} ISO creada correctamente.")

                    except Exception as e:
                        print(f"❌ Error durante la acción : {e}")


                # 👋 Exit
                # -----------------------    

                case "2":
                
                    print("👋 Saliendo de la consola de informacion del sistema.")
                    break            

            # 👋 Exit dialog
            # -----------------------    

            break_option = input("¿Deseas salir del subprograma de organización de archivos? (Yes/No): ")
            
            if break_option.lower() == "y" or break_option.lower() == "yes" :
                break
                break # the first break, breaks the match case , the second break the while
                
        
        except Exception as e:
            print(f"❌ Error de seleccion: {e}")    