# Marea Chatbot v1.1.0  (Multipurpose chatbot combining SLM , RAG and python code actions) 
# ---------------------------------------------------------------------------------------------------------------------------
# Purpose : Multipurpose chatbot combining SLM , RAG and python code actions in order to automate daily and repetitive tasks
# ---------------------------------------------------------------------------------------------------------------------------
# Author : Manuel Portero Leiva 
# ---------------------------------------------------------------------------------------------------------------------------


import warnings
# We write this code here to filter every warning
# ---------------------------------------------------------------------------------------------------------------------------
warnings.filterwarnings("ignore", message="pkg_resources is deprecated as an API")
# ---------------------------------------------------------------------------------------------------------------------------

import os
from sections.command_console import quick_notes_command_console
from sections.system_information import system_information
from sections.files_movements import files_movements
from sections.api_search import api_information_search
from sections.software_installator import software_installator
from constants import num_layout_equals
from sections.multimedia_conversor import multimedia_conversor
from sections.backup_flash_isos import backup_flash_isos

# ------------------------
# Main Code Section
# ------------------------

if __name__ == "__main__":


    while True :

        try:
        
            # ❌ Clean screen
            # ----------------

            os.system("clear")
        

            print("=" * num_layout_equals)
            print("👩‍💻  Marea Chatbot  —  Release v1.1.0   (Autor: Manuel Portero Leiva)")
            print("=" * num_layout_equals)
            print("🌊 Hola, soy Marea, tu asistente virtual.")
            print("=" * num_layout_equals)
            print("Selecciona una opción:")
            print("=" * num_layout_equals)
            print("⚙️   Opción 0: Información del sistema")
            print("📜  Opción 1: Movimientos de archivos")
            print("⚙️   Opción 2: Instalador de software / estructuras archivos")
            print("🧰  Opción 3: Generación de backups / USB flash / ISOs ")
            print("🎧  Opción 4: Conversor multimedia por IA")
            print("🔍  Opción 5: Buscador de datos vía API")
            print("🚀  Opción 6: Consulta IT y consulta de compandos rápidos")
            print("❌  Opción 7: Salir")
            print("=" * num_layout_equals)

            answer = input("👉  ¿Qué deseas hacer? (selecciona una opción): ")


            match answer:

                # ⚙️ System Information
                # ----------------------
                          
                case "0":
                    try:
                        print("⚙️ Entrando en información del sistema")
                        system_information()
                    except Exception as e:
                        print(f"❌ Error al realizar la accion : {e}")

                # 📜 Files movement
                # ----------------------

                case "1":
                    try:
                        print("📜 Entrando en movimientos de archivos")
                        files_movements()
                    except Exception as e:
                        print(f"❌ Error al realizar la accion : {e}")
                
                # ⚙️ Software and folder structure installation
                # -------------------------------------------------

                case "2":
                    try:
                        print("⚙️ Instalador de software / estructuras archivos")
                        software_installator()
                    except Exception as e:
                        print(f"❌ Error al realizar la accion : {e}")
 
                # 🧰 Backups / Flash USB and ISO creation
                # -------------------------------------------------

                case "3":
                    try:
                        print("🧰 Creacion de backups / flash USB y creación de ISOs")
                        backup_flash_isos()
                    except Exception as e:
                        print(f"❌ Error al realizar la accion : {e}")
                
                # 🎧 Multimedia AI conversor
                # -----------------------------------    
                
                case "4":
                    try:

                        multimedia_conversor()
                        
                    except Exception as e:
                        print(f"❌ Error al realizar la accion : {e}")
                

                # 🔍 MultiAPI information panel
                # -----------------------------------

                case "5":
                    try:
                        api_information_search()        
                    except Exception as e:
                        print(f"❌ Error al realizar la accion : {e}")


                # 🚀 Teminal command notes console
                # -----------------------------------

                case "6":
                    try:              
                        quick_notes_command_console()
                    except Exception as e:
                        print(f"❌ Error al realizar la accion : {e}")

                # 👋 Program Exit
                # -----------------------------------

                case "7":

                    print("Espero haberte ayudado 👋")
                    break
                    break # the first break, breaks the match case , the second break the while
                
                case _:

                    print("❌ No has seleccionado ninguna opción válida.")
                

            # 👋 Exit Dialog
            # -----------------------------------

            option_break = input("Deseas salir del programa ? (Yes/No): ")
            
            if option_break.lower() == "y" or option_break.lower() == "yes":
                print("Espero haberte ayudado 👋")
                break
                break # the first break, breaks the match case , the second break the while
                
        except Exception as e:
            print(f"❌ Error de seleccion: {e}")        