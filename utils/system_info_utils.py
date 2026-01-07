
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

# 🖥️ HARDWARE INFORMATION

def get_cpu_info():
    """CPU information"""
    return {
        'lscpu': run_command('lscpu'),
        'cpuinfo': run_command('cat /proc/cpuinfo'),
        'nproc': run_command('nproc')
    }

def get_memory_info():
    """RAM memory information"""
    return {
        'free': run_command('free -h'),
        'meminfo': run_command('cat /proc/meminfo'),
        'dmidecode': run_command('sudo dmidecode --type memory')
    }

def get_storage_info():
    """Disk and storage information"""
    return {
        'lsblk': run_command('lsblk'),
        'fdisk': run_command('sudo fdisk -l'),
        'df': run_command('df -hT'),
        'smartctl': run_command('sudo smartctl -a /dev/sda')
    }

def get_general_hardware():
    """General hardware information"""
    result = run_command('sudo lshw -html')
    if result['success']:
        with open('hardware.html', 'w') as f:
            f.write(result['output'])
        result['output'] = 'HTML report saved in hardware.html'
    
    return {
        'lshw_short': run_command('lshw -short'),
        'lshw_html': result,
        'hwinfo': run_command('hwinfo --short')
    }

# 🔧 SYSTEM INFORMATION

def get_os_info():
    """Operating system information"""
    return {
        'lsb_release': run_command('lsb_release -a'),
        'hostnamectl': run_command('hostnamectl'),
        'os_release': run_command('cat /etc/os-release'),
        'uname': run_command('uname -a')
    }

def get_kernel_info():
    """Kernel and modules information"""
    return {
        'dmesg': run_command('dmesg | tail -20'),
        'lsmod': run_command('lsmod')
    }

def get_kernel_module_info(module_name):
    """Specific kernel module information"""
    return run_command(f'modinfo {module_name}')

def get_uptime_info():
    """System uptime information"""
    return {
        'uptime': run_command('uptime'),
        'last_reboot': run_command('who -b')
    }

# 🌐 NETWORK AND CONNECTIVITY

def get_network_interfaces():
    """Network interfaces"""
    return {
        'ip_addr': run_command('ip addr show'),
        'netstat': run_command('netstat -tulpn'),
        'ss': run_command('ss -tulpn')
    }

def get_network_info():
    """General network information"""
    return {
        'hostname': run_command('hostname -I'),
        'route': run_command('route -n'),
        'resolv': run_command('cat /etc/resolv.conf')
    }

# 📊 SYSTEM PERFORMANCE

def get_processes_resources():
    """Processes and resources information"""
    return {
        'top': run_command('top -b -n 1 | head -20'),
    }

def get_system_stats():
    """System statistics"""
    return {
        'vmstat': run_command('vmstat 1 5'),
    }

# 📋 ALL-IN-ONE COMMANDS

def get_comprehensive_reports():
    """Complete system reports"""
    return {
        'inxi': run_command('inxi -Fxz'),
    }

