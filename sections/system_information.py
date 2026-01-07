from utils.system_info_utils import get_cpu_info,get_memory_info,get_storage_info,get_os_info
from utils.system_info_utils import get_network_interfaces,get_processes_resources,get_system_stats
from utils.system_info_utils import get_comprehensive_reports
from constants import num_layout_equals
import os

def system_information():

    while True :
        
        try:

            # ❌ Clean screen
            # ----------------

            os.system("clear")

            print("=" * num_layout_equals)
            print("⚙️  System Information  —  Autor: Manuel Portero Leiva")
            print("=" * num_layout_equals)
            print("Selecciona una opción:")
            print("=" * num_layout_equals)
            print("💻  Opción 0: Información del hardware y sistema operativo")
            print("🌐  Opción 1: Información de red y conectividad")
            print("📊  Opción 2: Rendimiento del sistema")
            print("📋  Opción 3: Informe completo")
            print("👋  Opcion 4: Salir")
            print("=" * num_layout_equals)

            answer = input("⚙️  Selecciona accion : ")

    
    
    


            match(answer):

                # 💻 Hardware Information
                # -----------------------------

                case "0": 
                    try:
                        
                        print("=== Información de Hardware ===")  
                        print("\n💻 CPU :")

                        cpu_info = get_cpu_info()
                        if cpu_info['nproc']['success']:
                            print(f"CPU Cores: {cpu_info['nproc']['output']}")
                        
                        print("\n🧠 Memoria :")

                        memory_info = get_memory_info()
                        if memory_info['free']['success']:
                            print(memory_info['free']['output'])
                        
                        print("\n💾 Almacenamiento :")

                        storage_info = get_storage_info()
                        if storage_info['df']['success']:
                            print(storage_info['df']['output'])
                        
                        print("\n=== Información del sistema ===")
                        os_info = get_os_info()
                        if os_info['lsb_release']['success']:
                            print("Sistema Operativo:")
                            print(os_info['lsb_release']['output'])

                    except Exception as e:
                        print(f"❌ Error durante la acción : {e}")

                # 🌐 Network Information
                # --------------------------

                case "1":
                    try:

                        print("\n=== Información de red ===")
                        network_info = get_network_interfaces()
                        if network_info['ip_addr']['success']:
                            print("Interfaces de red :")
                            print(network_info['ip_addr']['output'])

                    except Exception as e:
                        print(f"❌ Error durante la acción : {e}")

                # 📊 System Performance
                # ---------------------------

                case "2":
                    try:

                        print("\n=== Performance del sistema ===")
                        system_performance = get_processes_resources()
                        if system_performance['top']:
                            print("Informacion de recursos y procesos:")
                            print(system_performance['top']['output'])
                        system_statistics = get_system_stats()
                        if system_statistics['vmstat']:
                            print("Estadisticas del sistema:")
                            print(system_statistics['vmstat']['output'])

                    except Exception as e:
                        print(f"❌ Error durante la acción : {e}")


                # 📋 Full report
                # -----------------------    

                case "3":
                    try:

                        print("\n=== Informe Completo ===")
                        full_report = get_comprehensive_reports()
                        if full_report['inxi']:
                            print(full_report['inxi']['output'])

                    except Exception as e:
                        print(f"❌ Error durante la acción : {e}")

                # 👋 Exit
                # -----------------------    

                case "4":
                
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