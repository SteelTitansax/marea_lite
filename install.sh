#!/bin/bash

# Limpia la panalla 

clear

# Obtener ancho de la terminal
WIDTH=$(tput cols)

# Línea de "=" de ancho completo
LINE=$(printf '=%.0s' $(seq 1 $WIDTH))

# Mostrar línea superior
echo "$LINE"

# Mostrar "MAREA" centrado
printf "%*s\n" $(( (WIDTH + 5) / 2 )) "MAREA CHATBOT Installer v1.1.0 (Author : Manuel Portero Leiva)"

# Mostrar línea inferior
echo "$LINE"

# Actualiza repositorios e instala Python 3.11 y utilidades

echo "🐍 Instalando repositorio python3.11 y actualizando el sistema"

sudo add-apt-repository ppa:deadsnakes/ppa -y > /dev/null 2>&1

sudo apt-get update > /dev/null 2>&1 & sudo apt-get upgrade -y > /dev/null 2>&1

sudo apt-get install -y python3.11 python3.11-venv python3.11-distutils python3.11-dev build-essential curl > /dev/null 2>&1

# Instala ls paquetes de system info

echo "🖥️  Instalando los paquetes necesarios para la sección de información del sistema"

sudo apt-get install -y lshw hwinfo dmidecode smartmontools pciutils usbutils procps util-linux lsb-release net-tools iproute2 dnsutils inxi htop iotop sysstat fdisk parted python3 python3-pip > /dev/null 2>&1

# Instala los paquetes de multimedia conversor 
echo "🎬 Instalando los paquetes necesarios para la sección de conversion multimedia"

sudo apt-get install -y ffmpeg > /dev/null 2>&1

# Instala pip para Python 3.11

curl -sS https://bootstrap.pypa.io/get-pip.py | python3.11 > /dev/null 2>&1

# Crea un entorno virtual con Python 3.11
echo "🔧 Creando entorno virtual python"

python3.11 -m venv venv > /dev/null 2>&1

# Activa el entorno virtual
source venv/bin/activate > /dev/null 2>&1

# Verifica que Python y pip sean los correctos
python --version > /dev/null 2>&1
pip --version > /dev/null 2>&1

echo "🧠 Instalando Pytorch y CoquiTTS"

# Instala PyTorch y torchaudio (CPU-only)
pip install torch==2.3.0+cpu torchaudio==2.3.0+cpu --index-url https://download.pytorch.org/whl/cpu > /dev/null 2>&1

# Instala Coqui TTS
pip install --upgrade TTS > /dev/null 2>&1

# Instala SQLite3 
sudo apt install python3-dev build-essential libsqlite3-dev -y > /dev/null 2>&1
pip install --upgrade pip setuptools wheel > /dev/null 2>&1
pip install pysqlite3 > /dev/null 2>&1

# Crea base de datos de consulta
echo "Moviendo base de datos a estructura de archivos"
mkdir -p "$HOME/data" 

if [ -f "$HOME/data/database.db" ]; then
    echo "El archivo database.db  existe en $HOME/personal_agent."
else
    mv "$HOME/personal_agent/database.db" "$HOME/data/database.db"
    echo "Archivo movido correctamente."
fi

# Instala el resto de dependencias desde requirements.txt
echo "📦 Instalando el resto de dependencias de python y actualizando paquetes"

pip install -r requirements.txt > /dev/null 2>&1

# Upgrade torch (Remove in case of conflict )
pip install --upgrade torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu > /dev/null 2>&1


# Arranca el programa
echo "👩‍💻 Arrancando Marea chatbot"

python3 chatbot.py