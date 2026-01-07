from utils.software_installation_utils import (
    personal_computer_software_installation,
    install_python_packages,
    laptop_software_installation,
    tablet_software_installation,
    phone_software_installation,
    target_software_installation,
    search_software
)
from constants import (
    num_layout_equals,
    personal_computer_installation_packages,
    laptop_installation_packages,
    phone_installation_packages,
    tablet_installation_packages
)
from utils.utils import restore_backup
import os
import time

# ---------------------------------------------
# Función de reintentos
# ---------------------------------------------
def run_with_retry(func, *args, retries=5, delay=10, **kwargs):
    """
    Ejecuta una función con reintentos en caso de error.
    :param func: función a ejecutar
    :param args: argumentos posicionales
    :param retries: número máximo de intentos
    :param delay: segundos de espera entre intentos
    :param kwargs: argumentos nombrados
    :return: resultado de la función si tiene éxito
    :raises Exception: si falla después de todos los intentos
    """
    attempt = 0
    while attempt < retries:
        try:
            return func(*args, **kwargs)
        except Exception as e:
            attempt += 1
            print(f"⚠️  Error ejecutando {func.__name__} ({attempt}/{retries}): {e}")
            if attempt >= retries:
                print(f"❌ Se alcanzó el máximo de reintentos para {func.__name__}")
                raise
            print(f"⏳ Reintentando en {delay} segundos...")
            time.sleep(delay)

# ---------------------------------------------
# Instalador de software principal
# ---------------------------------------------
def software_installator():
    while True:
        try:
            # Limpia pantalla
            os.system("clear")

            # Menú
            print("=" * num_layout_equals)
            print("⚙️  Software Installer Console  —  Autor: Manuel Portero Leiva")
            print("=" * num_layout_equals)
            print("Selecciona una opción:")
            print("=" * num_layout_equals)
            print("🖥️    Opción 0: Instalar paquete en ordenador torre")
            print("💻   Opción 1: Instalar paquete en ordenador portátil")
            print("📟   Opción 2: Instalar paquete en dispositivo tablet") 
            print("📱   Opción 3: Instalar paquete en dispositivo móvil")
            print("🔎   Opción 4: Búsqueda e instalación de software específico")
            print("🔄   Opción 5: Movimiento de archivos desde backup")
            print("❌   Opción 6: Salir")
            print("=" * num_layout_equals)

            answer = input("⚙️  Selecciona acción: ")

            match(answer):
                # -----------------------------
                # Personal Computer
                # -----------------------------
                case "0":
                    try:
                        print("=== Instalando software en ordenador torre ===")  
                        software_installation = run_with_retry(
                            personal_computer_software_installation, 
                            personal_computer_installation_packages
                        )
                        for software_package in personal_computer_installation_packages:
                            if software_installation[software_package]['success']:
                                print(f"✅ {software_package} instalado correctamente.")
                            else:
                                print(f"❌ Error instalando {software_package}: {software_installation[software_package]['error']}") 

                        print("=== Instalando paquetes de Python ===")  
                        python_installation = run_with_retry(install_python_packages)
                        print(python_installation)
                        print("=== Instalación completada ===")  

                    except Exception as e:
                        print(f"❌ Error durante la acción: {e}")

                # -----------------------------
                # Laptop
                # -----------------------------
                case "1":
                    try:
                        print("=== Instalando software en ordenador portátil ===")  
                        software_installation = run_with_retry(
                            laptop_software_installation, 
                            laptop_installation_packages
                        )
                        for software_package in laptop_installation_packages:
                            if software_installation[software_package]['success']:
                                print(f"✅ {software_package} instalado correctamente.")
                            else:
                                print(f"❌ Error instalando {software_package}: {software_installation[software_package]['error']}") 

                        print("=== Instalando paquetes de Python ===")  
                        python_installation = run_with_retry(install_python_packages)
                        print(python_installation)
                        print("=== Instalación completada ===")  

                    except Exception as e:
                        print(f"❌ Error durante la acción: {e}")

                # -----------------------------
                # Tablet
                # -----------------------------
                case "2":
                    try:
                        print("=== Instalando software en dispositivo tablet ===")  
                        software_installation = run_with_retry(
                            tablet_software_installation, 
                            tablet_installation_packages
                        )
                        for software_package in tablet_installation_packages:
                            if software_installation[software_package]['success']:
                                print(f"✅ {software_package} instalado correctamente.")
                            else:
                                print(f"❌ Error instalando {software_package}: {software_installation[software_package]['error']}") 

                        print("=== Instalando paquetes de Python ===")  
                        python_installation = run_with_retry(install_python_packages)
                        print(python_installation)
                        print("=== Instalación completada ===")  

                    except Exception as e:
                        print(f"❌ Error durante la acción: {e}")

                # -----------------------------
                # Phone
                # -----------------------------
                case "3":
                    try:
                        print("=== Instalando software en dispositivo móvil ===")  
                        software_installation = run_with_retry(
                            phone_software_installation, 
                            phone_installation_packages
                        )
                        for software_package in phone_installation_packages:
                            if software_installation[software_package]['success']:
                                print(f"✅ {software_package} instalado correctamente.")
                            else:
                                print(f"❌ Error instalando {software_package}: {software_installation[software_package]['error']}") 

                        print("=== Instalando paquetes de Python ===")  
                        python_installation = run_with_retry(install_python_packages)
                        print(python_installation)
                        print("=== Instalación completada ===")  

                    except Exception as e:
                        print(f"❌ Error durante la acción: {e}")

                # -----------------------------
                # Target software
                # -----------------------------
                case "4":
                    try:
                        print("=== Instalando software específico ===")  
                        target_software = input("Por favor introduzca el software a buscar: ")
                        search_result = run_with_retry(search_software, target_software)
                        print(search_result[target_software]['output'])

                        continue_answer = input("Deseas instalar algún paquete encontrado (Yes/No): ")
                        if continue_answer.lower() in ["no", "n"]:
                            break

                        target_install_software = input("Por favor introduzca software a instalar: ")
                        software_installation = run_with_retry(target_software_installation, target_install_software)
                        if software_installation[target_install_software]['success']:
                            print(f"✅ {target_install_software} instalado correctamente.")
                        else:
                            print(f"❌ Error instalando {target_install_software}: {software_installation[target_install_software]['error']}") 

                        print("=== Instalación completada ===")  

                    except Exception as e:
                        print(f"❌ Error durante la acción: {e}")

                # -----------------------------
                # Restore backup
                # -----------------------------
                case "5":
                    try:
                        drive_name = input("Por favor introduce el nombre del external drive: ")
                        username = input("Por favor introduce el username de la computadora: ")
                        one_folder = input("Quieres restaurar el backup usual o solo una carpeta (Yes/No)?")
                        if one_folder.lower() == "y" or one_folder.lower() == "yes" :
                            one_folder_name = input("Introduce el nombre de la carpeta a restaurar : ")
                            one_folder = True
                        else:
                            one_folder_name = ""
                            one_folder = False
                        verbose_input = input("Quieres correr el backup en modo verbose? (Yes/No): ")
                        verbose = verbose_input.lower() in ["yes", "y"]
                        restore_backup(drive_name, username, verbose=verbose,one_folder_name=one_folder_name, one_folder=one_folder)
                    except Exception as e:
                        print(f"❌ Error al realizar la acción: {e}")

                # -----------------------------
                # Exit
                # -----------------------------
                case "6":
                    print("👋 Saliendo de la consola de instalación de software.")
                    break

            # Pregunta si salir del subprograma
            break_option = input("¿Deseas salir del subprograma de instalación? (Yes/No): ")
            if break_option.lower() in ["y", "yes"]:
                break

        except Exception as e:
            print(f"❌ Error de selección: {e}")
