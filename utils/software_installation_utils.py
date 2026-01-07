from constants import python_packages
import subprocess

def run_command(command, timeout=30):
    """
    Helper function to execute system commands
    
    Args:
        command (str): Command to execute
        timeout (int): Maximum execution time
    
    Returns:
        dict: Result with 'success', 'output' and 'error'
    """
    try:
        result = subprocess.run(
            command, 
            shell=True, 
            capture_output=True, 
            text=True, 
            timeout=timeout
        )
        return {
            'success': result.returncode == 0,
            'output': result.stdout.strip(),
            'error': result.stderr.strip(),
            'return_code': result.returncode
        }
    except subprocess.TimeoutExpired:
        return {'success': False, 'error': 'Timeout expired', 'output': ''}
    except FileNotFoundError:
        return {'success': False, 'error': f'Command not found: {command}', 'output': ''}
    except Exception as e:
        return {'success': False, 'error': str(e), 'output': ''}

# Search software 

def search_software(target_software):
    return {
        f'{target_software}': run_command(f'sudo apt-cache search {target_software}'),
    }

# Target software installation 

def target_software_installation(target_software):
    return {
        f'{target_software}': run_command(f'sudo apt-get install {target_software} -y'),
    }

def personal_computer_software_installation(personal_computer_installation_packages):
        return {pkg: run_command(cmd) for pkg, cmd in personal_computer_installation_packages.items()}


# 🖥️ Laptop computer software installation

def laptop_software_installation(laptop_installation_packages):
    return {pkg: run_command(cmd) for pkg, cmd in laptop_installation_packages.items()}


def phone_software_installation(phone_installation_packages):
    return {pkg: run_command(cmd) for pkg, cmd in phone_installation_packages.items()}

def tablet_software_installation(tablet_installation_packages):
        return {pkg: run_command(cmd) for pkg, cmd in tablet_installation_packages.items()}



def install_python_packages():
    
    results = {}
    print(f"📦 Instalando {len(python_packages)} paquetes Python...")
    
    # Install in batches for avoiding timeouts
    batch_size = 20
    for i in range(0, len(python_packages), batch_size):
        batch = python_packages[i:i + batch_size]
        print(f"🔧 Instalando lote {i//batch_size + 1}/{(len(python_packages)-1)//batch_size + 1}...")
        
        for package in batch:
            try:
                result = run_command(f'pip install {package}', timeout=120)
                results[package] = result
                if result['success']:
                    print(f"   ✅ {package}")
                else:
                    print(f"   ❌ {package}: {result['error']}")
            except Exception as e:
                results[package] = {'success': False, 'error': str(e)}
                print(f"   ❌ {package}: {e}")
    
    print("🎉 Instalación de paquetes Python completada!")
    return results