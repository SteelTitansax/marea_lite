import os 
from constants import bash_commands,powershell_commands,python_commands,javascript_commands,sql_commands,num_layout_equals
from utils.command_console_utils import search_sqllite_information,display_technologies,insert_sqlite_information
def quick_notes_command_console():
    
    while True :

        try:

            # ❌ Clean screen
            # ----------------
            
            os.system("clear")

            print("=" * num_layout_equals)
            print("🖥️  Busqueda & Commandos de Consola  —  Autor: Manuel Portero Leiva")
            print("=" * num_layout_equals)
            print("Selecciona una opción:")
            print("=" * num_layout_equals)            
            print("🐚  Opción 1: Notas consola de comandos Bash")
            print("⚡  Opción 2: Notas consola de comandos PowerShell")
            print("🐍  Opción 3: Notas consola de comandos Python")
            print("📜  Opción 4: Notas consola de comandos JavaScript")
            print("💾  Opción 5: Notas consola de comandos SQL")
            print("🔍  Opción 6: Buscar información en Notas personales")
            print("💾  Opción 7: Añadir información en Notas personales")
            print("👋  Opción 8: Salir")
            print("=" * num_layout_equals)

        
            answer = input("🖥️  Selecciona comando :")
            
            match(answer):            
      
                # 🐚 Bash console commands
                # ------------------------------
        
                case "1": 
                    try:
                        print("🐚  Mostrando lista de comandos comunes para una consola bash")
                        print(bash_commands)
                    except Exception as e:
                        print(f"Error: {e}")

                # ⚡  Powershell console commands
                # ------------------------------
                
                case "2":
                    try:
                        print("⚡ Mostrando lista de comandos comunes para una consola Powershell")
                        print(powershell_commands)
                    except Exception as e:
                        print(f"Error: {e}")

                # 🐍 Python console commands
                # ------------------------------
                
                case "3": 
                    try:
                        print("🐍 Mostrando lista de comandos comunes para una consola python")
                        print(python_commands)
                    except Exception as e:
                        print(f"Error: {e}")


                # 📜 JavaScript console commands
                # ------------------------------
                
                case "4": 
                    try:
                        print("📜 Mostrando lista de comandos comunes para una consola node")
                        print(javascript_commands)
                    except Exception as e:
                        print(f"Error: {e}")

                # 💾 SQL console commands
                # ------------------------------
                
                case "5": 
                    try:
                        print("💾 Mostrando lista de comandos comunes para una consola SQL")
                        print(sql_commands)
                    except Exception as e:
                        print(f"Error: {e}")


                # 📜  Opción 6: Buscar información en Notas personales
                # --------------------------------------------------------
                
                case "6":
                    try:
                        print("💾 Buscar información en Notas personales ..........")
                        print("Mostrando tecnologías disponibles")
                        print("=" * num_layout_equals)
                        
                        technologies = display_technologies()
                        if technologies:
                            for tech in technologies:
                                print(tech[0]) 
                        else:
                            print("No hay tecnologías registradas.")
                        
                        print("=" * num_layout_equals)

                        query = input("Por favor introduzca tecnología de consulta: ").strip()
                        results = search_sqllite_information(query)

                        if results:
                            print(f"Resultados de la consulta - Tecnología: {query}")
                            print("=" * num_layout_equals)
                            for result in results:
                                print(f"\n{result[2]}")
                            print(f"\n")
                        else:
                            print("No se han encontrado resultados.")

                    except Exception as e:
                        print(f"Error: {e}")

                
                # 💾  Opción 7: Añadir información en Notas personales
                # --------------------------------------------------------
                
                case "7": 
                    try:
                        print("💾 Añadiendo información en Notas personales")
                        print("=" * num_layout_equals)
                        technology = input("Por favor introduzca la technología : ")
                        post = input("Por favor introduzca contenido de post : ")
                        if not(technology == "") or not(post == "") :
                            result = insert_sqlite_information(technology,post)
                            if result: 
                                print("Post insertado correctamente.")
                        else:
                            print("Por favor introduce valores de tecnología y contenido correctos (ningún campo en blanco)")
                        
                    except Exception as e:
                        print(f"Error: {e}")

                
                # 👋 Exit
                # ------------------------------
                
                case "8":
                    
                    print("👋 Saliendo de la command console...")
                    break      
    
                case _:

                    print("❌ Seleccion no válida. Introduzca seleccion valida o 'salir' para finalizar programa.")

            # 👋 Exit dialog
            # ------------------------------
            
            break_option = input("¿Deseas salir del subprograma de organización de archivos? (Yes/No): ")
            if break_option.lower() == "y" or break_option.lower() == "yes" :
                break
                break # the first break, breaks the match case , the second break the while
                
        
        except Exception as e:
            print(f"❌ Error de seleccion: {e}")    