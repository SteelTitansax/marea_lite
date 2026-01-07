import os
from pathlib import Path

# Input and output dirs
# ----------------------
home = Path.home()

INPUT_DIR = Path(f"{home}/marea_lite/chatbot_input")
OUTPUT_DIR = Path(f"{home}/marea_lite/chatbot_output")
DATA_DIR = Path(f"{home}/Data")

# Get terminal width 
# ---------------------
terminal_width = os.get_terminal_size().columns

# Adjust the number of "=" to the terminal width
# -----------------------------------------------
num_layout_equals = terminal_width

# Config 
# ---------------------

DB_PATH = "./data.db"
FAISS_INDEX_PATH = "./faiss_index"
sentence_transformer= "sentence-transformers/all-MiniLM-L6-v2"

# Marea Prompts 
# ---------------------

system_prompt_free = """

CONTEXTO:

- Eres Marea, un agente de IA altamente capacitado. Tu objetivo es ayudar a los usuarios respondiendo sus preguntas de manera clara, precisa y concisa.
- Tu creador y programador es Manuel Portero, un programador con 5 años de experiencia en automatismos, desarrollo web y AI. Intenta responder de manera personalizada ante el nombre de este usuario.

NOTAS:

- Está bien no encontrar respuestas y decir que no tienes información.

IMPORTANTE:

- Sé claro y fácil de entender.
- Usa un tono profesional y amigable.
- Si hay dudas en la pregunta, pide aclaración antes de responder.
- Mantente siempre dentro del marco proporcionado por este contexto.
- Siempre que te pregunten una pregunta directa a ti como agente responde en primera persona. Por otra parte tu genero es feminino asi que responde en femenino si se refieren a ti.

AGRADECIMIENTOS:

- Siempre que el usuario diga “gracias”, “gracias por tu ayuda” u otra forma de agradecimiento, responde con:
  → “De nada, siempre dispuesta a ayudarte :).”
 

"""


system_prompt = """

CONTEXTO:

Eres Marea, un agente de IA altamente capacitado. Tu objetivo es ayudar a los usuarios respondiendo sus preguntas de manera clara, precisa y concisa.
Tienes acceso a una base de datos de documentos que puedes usar para proporcionar respuestas más detalladas.
Responde de la manera más útil posible y no dudes en proporcionar ejemplos o detalles cuando sea necesario.
Si no tienes suficiente información o si la pregunta no está clara, está bien decir que no tienes información suficiente para responder.
Tu creador y programador es Manuel Portero, un programador con 5 años de experiencia en automatismos, desarrollo web y AI. Intenta responder de manera personalizada ante el nombre de este usuario.

NOTAS:

- Está bien no encontrar respuestas y decir que no tienes información.
- No inventes respuestas.
- Si la pregunta está fuera de tu ámbito o de los documentos, simplemente indícalo.
- Puedes sugerir al usuario buscar fuentes externas si crees que es útil.
- Respuesta (si no tienes suficiente información, responde "No tengo información suficiente para responder con precisión."):

IMPORTANTE:

- Sé claro y fácil de entender.
- Usa un tono profesional y amigable.
- Si hay dudas en la pregunta, pide aclaración antes de responder.
- Mantente siempre dentro del marco proporcionado por este contexto.
- Siempre que te pregunten una pregunta directa a ti como agente responde en primera persona. Por otra parte tu genero es feminino asi que responde en femenino si se refieren a ti.

AGRADECIMIENTOS:

- Siempre que el usuario diga “gracias”, “gracias por tu ayuda” u otra forma de agradecimiento, responde con:
  → “De nada, siempre dispuesta a ayudarte :).”
 

"""

# PromptTemplate for RetrievalQA
# ---------------------------------------

qa_prompt_template = f"""{system_prompt}

Usa únicamente el siguiente contexto para responder la pregunta. Si la respuesta no está explícitamente en el contexto, responde: "No tengo información suficiente para responder con precisión."

Contexto relevante:
{{context}}

Pregunta: {{question}}
Respuesta:"""



# Constant quick commands console
# --------------------------------------

bash_commands = """
            
## 📁 Navegación

ls        # Lista archivos y carpetas  
cd        # Cambia de directorio  
pwd       # Muestra la ruta del directorio actual  
tree      # Muestra estructura de carpetas en forma de árbol  

## 🗂️ Gestión de archivos y carpetas

touch     # Crea un archivo vacío  
mkdir     # Crea un nuevo directorio  
cp        # Copia archivos o carpetas  
mv        # Mueve o renombra archivos  
rm        # Elimina archivos  
rmdir     # Elimina carpetas  

## 📖 Lectura de archivos

cat       # Muestra contenido de un archivo  
less      # Visualiza un archivo página por página  
head      # Muestra las primeras líneas de un archivo  
tail      # Muestra las últimas líneas de un archivo  

## 🔐 Permisos de archivos

chmod     # Cambia permisos de un archivo  
chown     # Cambia propietario de un archivo  
sudo      # Ejecuta comandos como administrador  

## 🔍 Búsqueda de ficheros

find      # Busca archivos en directorios  
grep      # Busca texto dentro de archivos  

## 🌐 Utilidades de red

ping      # Comprueba conexión con una dirección  
curl      # Realiza peticiones HTTP  
wget      # Descarga archivos desde una URL (instalable en macOS)  

## 🖥️ Procesos del sistema

top       # Muestra procesos en ejecución  
ps        # Lista procesos activos  
kill      # Termina un proceso  
df -h     # Muestra espacio disponible en discos (legible)  
du -sh    # Muestra tamaño de archivos y carpetas (legible)  
uptime    # Muestra tiempo encendido y carga del sistema  
clear     # Limpia la terminal  

## 🛠️ Utilidades de sistema

echo      # Imprime texto en la terminal  
history   # Muestra historial de comandos  
man       # Muestra el manual de un comando  
nano      # Editor de texto básico  
vim       # Editor de texto avanzado  

            
        """

powershell_commands = """
        
            
🖥 PowerShell

📁 Navegación
ls # Lista archivos y carpetas
cd ruta # Cambia de directorio
pwd # Muestra la ruta del directorio actual
tree /f # Muestra estructura de carpetas en forma de árbol

🗂️ Gestión de archivos y carpetas
New-Item archivo.txt # Crea un archivo vacío
New-Item -ItemType Directory carpeta # Crea un nuevo directorio
Copy-Item src.txt dst.txt # Copia archivos o carpetas
Move-Item src.txt dst.txt # Mueve o renombra archivos
Remove-Item archivo.txt # Elimina archivos
Remove-Item carpeta -Recurse # Elimina carpetas

📖 Lectura de archivos
Get-Content archivo.txt # Muestra contenido de un archivo
more archivo.txt # Visualiza un archivo página por página
Get-Content archivo.txt -TotalCount 10 # Muestra las primeras líneas de un archivo
Get-Content archivo.txt -Tail 10 # Muestra las últimas líneas de un archivo

🔐 Permisos de archivos
icacls archivo.txt /grant usuario:F # Cambia permisos de un archivo
icacls archivo.txt /setowner usuario # Cambia propietario de un archivo
Start-Process powershell -Verb runAs # Ejecuta comandos como administrador

🔍 Búsqueda de ficheros
Get-ChildItem -Recurse -Filter *.txt # Busca archivos en directorios
Select-String "texto" archivo.txt # Busca texto dentro de archivos

🌐 Utilidades de red
ping google.com # Comprueba conexión con una dirección
curl https://example.com # Realiza peticiones HTTP
Invoke-WebRequest https://example.com # Descarga archivos desde una URL

🖥️ Procesos del sistema
Get-Process # Lista procesos activos
Stop-Process -Id <PID> # Termina un proceso
Get-PSDrive # Muestra espacio en discos
Get-ChildItem -Recurse | Measure-Object -Sum Length # Tamaño total de archivos
Get-Uptime # Muestra tiempo encendido del sistema
clear # Limpia la terminal

🛠️ Utilidades de sistema
echo "texto" # Imprime texto en la terminal
Get-History # Muestra historial de comandos
Get-Help comando # Muestra el manual de un comando
notepad archivo.txt # Editor de texto básico
vim archivo.txt # Editor de texto avanzado (si instalado)
                
        """

python_commands = """
📁 Navegación
import os; os.listdir() # Lista archivos y carpetas
import os; os.chdir('ruta') # Cambia de directorio
import os; os.getcwd() # Muestra la ruta del directorio actual
import os; list(os.walk('.')) # Muestra estructura de carpetas en árbol

🗂️ Gestión de archivos y carpetas
open('archivo.txt','w').close() # Crea un archivo vacío
import os; os.mkdir('carpeta') # Crea un nuevo directorio
import shutil; shutil.copy('src.txt','dst.txt') # Copia archivos o carpetas
import os; os.rename('src.txt','dst.txt') # Mueve o renombra archivos
import os; os.remove('archivo.txt') # Elimina archivos
import shutil; shutil.rmtree('carpeta') # Elimina carpetas

📖 Lectura de archivos
open('archivo.txt').read() # Muestra contenido de un archivo
import pydoc; pydoc.pager(open('archivo.txt').read()) # Visualiza archivo página por página
import itertools; list(itertools.islice(open('archivo.txt'),10)) # Primeras líneas
from collections import deque; deque(open('archivo.txt'), maxlen=10) # Últimas líneas

🔐 Permisos de archivos
import os; os.chmod('archivo.txt', 0o777) # Cambia permisos de un archivo
import shutil; shutil.chown('archivo.txt', user='usuario') # Cambia propietario de un archivo

Ejecutar como admin depende del sistema, no hay comando directo
🔍 Búsqueda de ficheros
import glob; glob.glob('**/*.txt', recursive=True) # Busca archivos
import re; re.findall('texto', open('archivo.txt').read()) # Busca texto dentro de archivos

🌐 Utilidades de red
import os; os.system('ping google.com') # Comprueba conexión con una dirección
import urllib.request; urllib.request.urlopen('https://example.com').read() # Petición HTTP
import urllib.request; urllib.request.urlretrieve('https://example.com/archivo.zip', 'archivo.zip') # Descargar archivo

🖥️ Procesos del sistema
import os; os.system('tasklist') # Lista procesos (Windows)
import os; os.system('kill <PID>') # Termina un proceso
import shutil; shutil.disk_usage('.') # Muestra espacio en discos
import os; sum(os.path.getsize(f) for f in os.listdir('.') if os.path.isfile(f)) # Tamaño total
import os; os.system('uptime') # Tiempo encendido del sistema
import os; os.system('clear') # Limpia la terminal

🛠️ Utilidades de sistema
print("texto") # Imprime texto en consola
import readline; readline.get_current_history_length() # Historial de comandos
help(str) # Muestra ayuda de un objeto/comando
import os; os.system('nano archivo.txt') # Editor de texto básico
import os; os.system('vim archivo.txt') # Editor de texto avanzado            
                """

javascript_commands = """
            📦 JavaScript (Node.js)
📁 Navegación
const fs = require('fs'); fs.readdirSync('.') # Lista archivos y carpetas
process.chdir('ruta') # Cambia de directorio
process.cwd() # Muestra la ruta actual
// Usar paquete 'tree-cli' para estructura de árbol

🗂️ Gestión de archivos y carpetas
fs.writeFileSync('archivo.txt', '') # Crea archivo vacío
fs.mkdirSync('carpeta') # Crea nuevo directorio
fs.copyFileSync('src.txt','dst.txt') # Copia archivo
fs.renameSync('src.txt','dst.txt') # Mueve o renombra archivo
fs.unlinkSync('archivo.txt') # Elimina archivo
fs.rmdirSync('carpeta', { recursive: true }) # Elimina carpeta

📖 Lectura de archivos
fs.readFileSync('archivo.txt','utf8') # Muestra contenido de un archivo
// No hay paginación nativa, usar 'readline'
fs.readFileSync('archivo.txt','utf8').split('\n').slice(0,10) # Primeras líneas
fs.readFileSync('archivo.txt','utf8').split('\n').slice(-10) # Últimas líneas

🔐 Permisos de archivos
fs.chmodSync('archivo.txt', 0o777) # Cambia permisos de un archivo
// Cambiar propietario no disponible de forma nativa en Node estándar

🔍 Búsqueda de ficheros
const glob = require('glob'); glob.sync('**/*.txt') # Busca archivos
fs.readFileSync('archivo.txt','utf8').includes('texto') # Busca texto en archivos

🌐 Utilidades de red
const { execSync } = require('child_process'); execSync('ping google.com', {stdio:'inherit'}) # Ping
const https = require('https'); https.get('https://example.com', res => {res.on('data', d => process.stdout.write(d));}); // Petición HTTP
const https2 = require('https'); const fs2 = require('fs'); https2.get('https://example.com/archivo.zip', res => {res.pipe(fs2.createWriteStream('archivo.zip'));}); // Descargar archivo

🖥️ Procesos del sistema
execSync('tasklist', {stdio:'inherit'}) # Lista procesos (Windows)
execSync('kill <PID>', {stdio:'inherit'}) # Termina proceso
fs.statSync('/') # Muestra espacio de disco (requiere cálculo)
execSync('uptime', {stdio:'inherit'}) # Tiempo encendido
console.clear() # Limpia la terminal

🛠️ Utilidades de sistema
console.log("texto") # Imprime texto
// Historial no disponible de forma nativa
execSync('man ls', {stdio:'inherit'}) # Muestra manual (Linux/macOS)
execSync('nano archivo.txt', {stdio:'inherit'}) # Editor básico
execSync('vim archivo.txt', {stdio:'inherit'}) # Editor avanzado
            """

sql_commands ="""
            🗄 SQL (genérico)
📁 Navegación
-- No aplica en SQL

🗂️ Gestión de datos
CREATE TABLE tabla (...); # Crea una nueva tabla
INSERT INTO tabla VALUES (...); # Inserta datos
UPDATE tabla SET columna=valor WHERE ...; # Modifica datos
DELETE FROM tabla WHERE ...; # Elimina datos

📖 Lectura de datos
SELECT * FROM tabla; # Muestra todos los registros
SELECT * FROM tabla LIMIT 10; # Primeros registros
SELECT * FROM tabla ORDER BY id DESC LIMIT 10; # Últimos registros

🔐 Permisos de base de datos
GRANT SELECT, INSERT ON tabla TO usuario; # Da permisos a un usuario
REVOKE SELECT ON tabla FROM usuario; # Revoca permisos

🔍 Búsqueda de datos
SELECT * FROM tabla WHERE columna LIKE '%texto%'; # Busca texto
SELECT * FROM tabla WHERE columna = valor; # Coincidencia exacta

🌐 Utilidades de red
-- Depende del motor, en MySQL por ejemplo:
SHOW VARIABLES LIKE 'hostname'; # Muestra el host actual

🖥️ Procesos del sistema
SHOW PROCESSLIST; # Lista procesos/conexiones activas
KILL <id_proceso>; # Termina un proceso/conexión

🛠️ Utilidades
SHOW TABLES; # Lista tablas
DESCRIBE tabla; # Muestra estructura de tabla
EXPLAIN SELECT ...; # Plan de ejecución
EXIT; # Sale de la consola SQL
            """


# Software packages
# -------------------------------

personal_computer_installation_packages = {
        'system_update': 'sudo apt-get update && sudo apt-get upgrade -y',
        'snapd_install': 'sudo apt-get install snapd -y',
        'genisoimage' : 'sudo apt-get install genisoimage -y',
        'snapd_enable': 'sudo systemctl enable --now snapd.socket',
        'telegram': 'sudo add-apt-repository ppa:atareao/telegram -y && sudo apt-get update && sudo apt install telegram -y',
        'chromium': 'sudo apt-get install chromium-browser -y',
        'virtualbox': 'sudo apt-get install virtualbox -y',
        'git': 'sudo apt-get install git -y',
        'github_cli': 'sudo apt-get install gh -y',
        'vim': 'sudo apt-get install vim -y',
        'docker': 'sudo apt-get install docker.io -y',
        'python_pip': 'sudo apt-get install python3 python3-pip python3-venv -y',
        'curl_wget': 'sudo apt-get install curl wget -y',
        'ollama': 'curl -fsSL https://ollama.ai/install.sh | sh',
        'ollama_service': 'sudo systemctl enable ollama && sudo systemctl start ollama',
        'cura_slicer': 'sudo snap install cura-slicer --classic',
        'vscode': 'sudo snap install code --classic',
        'whatsapp': 'sudo snap install whatsapp-for-linux',
        'blender': 'sudo snap install blender --classic',
        'gimp': 'sudo snap install gimp',
        'pycharm': 'sudo snap install pycharm-community --classic',
        'nodejs': 'sudo apt-get install nodejs npm -y',
        'ffmpeg': 'sudo apt-get install ffmpeg -y',
        'htop': 'sudo apt-get install htop -y',
        'nano': 'sudo apt-get install nano -y',
        'wget': 'sudo apt-get install wget -y',
        'zip': 'sudo apt-get install zip unzip -y',
        'rsync': 'sudo apt-get install rsync -y',
        'ssh': 'sudo apt-get install openssh-client openssh-server -y',
        'python_development': 'sudo apt-get install python3-dev python3-venv build-essential -y',
        'jq': 'sudo apt-get install jq -y',
        'tree': 'sudo apt-get install tree -y',
        'screen': 'sudo apt-get install screen -y',
        'tmux': 'sudo apt-get install tmux -y',
        'neofetch': 'sudo apt-get install neofetch -y',
        'termux_api': 'pkg install termux-api -y',
        'python_packages': 'pip install requests beautifulsoup4 pandas numpy matplotlib jupyter seaborn scikit-learn',
        'network_tools': 'sudo apt-get install net-tools iproute2 dnsutils -y',
        'process_tools': 'sudo apt-get install procps htop iotop -y',
        'system_monitoring': 'sudo apt-get install sysstat inxi -y'
    }

laptop_installation_packages = {
        'system_update': 'sudo apt-get update && sudo apt-get upgrade -y',
        'snapd_install': 'sudo apt-get install snapd -y',
        'snapd_enable': 'sudo systemctl enable --now snapd.socket',
        'telegram': 'sudo add-apt-repository ppa:atareao/telegram -y && sudo apt-get update && sudo apt install telegram -y',
        'chromium': 'sudo apt-get install chromium-browser -y',
        'virtualbox': 'sudo apt-get install virtualbox -y',
        'git': 'sudo apt-get install git -y',
        'github_cli': 'sudo apt-get install gh -y',
        'vim': 'sudo apt-get install vim -y',
        'docker': 'sudo apt-get install docker.io -y',
        'python_pip': 'sudo apt-get install python3 python3-pip python3-venv -y',
        'curl_wget': 'sudo apt-get install curl wget -y',
        'ollama': 'curl -fsSL https://ollama.ai/install.sh | sh',
        'ollama_service': 'sudo systemctl enable ollama && sudo systemctl start ollama',
        'cura_slicer': 'sudo snap install cura-slicer --classic',
        'vscode': 'sudo snap install code --classic',
        'whatsapp': 'sudo snap install whatsapp-for-linux',
        'blender': 'sudo snap install blender --classic',
        'gimp': 'sudo snap install gimp',
        'pycharm': 'sudo snap install pycharm-community --classic',
        'nodejs': 'sudo apt-get install nodejs npm -y',
        'ffmpeg': 'sudo apt-get install ffmpeg -y',
        'htop': 'sudo apt-get install htop -y',
        'nano': 'sudo apt-get install nano -y',
        'wget': 'sudo apt-get install wget -y',
        'zip': 'sudo apt-get install zip unzip -y',
        'rsync': 'sudo apt-get install rsync -y',
        'ssh': 'sudo apt-get install openssh-client openssh-server -y',
        'python_development': 'sudo apt-get install python3-dev python3-venv build-essential -y',
        'jq': 'sudo apt-get install jq -y',
        'tree': 'sudo apt-get install tree -y',
        'screen': 'sudo apt-get install screen -y',
        'tmux': 'sudo apt-get install tmux -y',
        'neofetch': 'sudo apt-get install neofetch -y',
        'termux_api': 'pkg install termux-api -y',
        'python_packages': 'pip install requests beautifulsoup4 pandas numpy matplotlib jupyter seaborn scikit-learn',
        'network_tools': 'sudo apt-get install net-tools iproute2 dnsutils -y',
        'process_tools': 'sudo apt-get install procps htop iotop -y',
        'system_monitoring': 'sudo apt-get install sysstat inxi -y'
    }

phone_installation_packages = {
    'system_update': 'sudo apt-get update && sudo apt-get upgrade -y',
    'snapd_install': 'sudo apt-get install snapd -y',
    'snapd_enable': 'sudo systemctl enable --now snapd.socket',
    'git': 'sudo apt-get install git -y',
    'github_cli': 'sudo apt-get install gh -y',
    'vim': 'sudo apt-get install vim -y',
    'docker': 'sudo apt-get install docker.io -y',
    'python_pip': 'sudo apt-get install python3 python3-pip python3-venv -y',
    'curl_wget': 'sudo apt-get install curl wget -y',
    'ollama': 'curl -fsSL https://ollama.ai/install.sh | sh',
    'ollama_service': 'sudo systemctl enable ollama && sudo systemctl start ollama',
    'nodejs': 'sudo apt-get install nodejs npm -y',
    'ffmpeg': 'sudo apt-get install ffmpeg -y',
    'htop': 'sudo apt-get install htop -y',
    'nano': 'sudo apt-get install nano -y',
    'wget': 'sudo apt-get install wget -y',
    'zip': 'sudo apt-get install zip unzip -y',
    'rsync': 'sudo apt-get install rsync -y',
    'ssh': 'sudo apt-get install openssh-client openssh-server -y',
    'python_development': 'sudo apt-get install python3-dev python3-venv build-essential -y',
    'jq': 'sudo apt-get install jq -y',
    'tree': 'sudo apt-get install tree -y',
    'screen': 'sudo apt-get install screen -y',
    'tmux': 'sudo apt-get install tmux -y',
    'neofetch': 'sudo apt-get install neofetch -y',
    'termux_api': 'pkg install termux-api -y',
    'python_packages': 'pip install requests beautifulsoup4 pandas numpy matplotlib jupyter seaborn scikit-learn',
    'network_tools': 'sudo apt-get install net-tools iproute2 dnsutils -y',
    'process_tools': 'sudo apt-get install procps htop iotop -y',
    'system_monitoring': 'sudo apt-get install sysstat inxi -y'
}

tablet_installation_packages ={
    'system_update': 'sudo apt-get update && sudo apt-get upgrade -y',
    'snapd_install': 'sudo apt-get install snapd -y',
    'snapd_enable': 'sudo systemctl enable --now snapd.socket',
    'git': 'sudo apt-get install git -y',
    'github_cli': 'sudo apt-get install gh -y',
    'vim': 'sudo apt-get install vim -y',
    'docker': 'sudo apt-get install docker.io -y',
    'python_pip': 'sudo apt-get install python3 python3-pip python3-venv -y',
    'curl_wget': 'sudo apt-get install curl wget -y',
    'ollama': 'curl -fsSL https://ollama.ai/install.sh | sh',
    'ollama_service': 'sudo systemctl enable ollama && sudo systemctl start ollama',
    'nodejs': 'sudo apt-get install nodejs npm -y',
    'ffmpeg': 'sudo apt-get install ffmpeg -y',
    'htop': 'sudo apt-get install htop -y',
    'nano': 'sudo apt-get install nano -y',
    'wget': 'sudo apt-get install wget -y',
    'zip': 'sudo apt-get install zip unzip -y',
    'rsync': 'sudo apt-get install rsync -y',
    'ssh': 'sudo apt-get install openssh-client openssh-server -y',
    'python_development': 'sudo apt-get install python3-dev python3-venv build-essential -y',
    'jq': 'sudo apt-get install jq -y',
    'tree': 'sudo apt-get install tree -y',
    'screen': 'sudo apt-get install screen -y',
    'tmux': 'sudo apt-get install tmux -y',
    'neofetch': 'sudo apt-get install neofetch -y',
    'termux_api': 'pkg install termux-api -y',
    'python_packages': 'pip install requests beautifulsoup4 pandas numpy matplotlib jupyter seaborn scikit-learn',
    'network_tools': 'sudo apt-get install net-tools iproute2 dnsutils -y',
    'process_tools': 'sudo apt-get install procps htop iotop -y',
    'system_monitoring': 'sudo apt-get install sysstat inxi -y'
}

python_packages = [
        'absl-py', 'aiobotocore', 'aiohappyeyeballs', 'aiohttp', 'aioitertools',
        'aiosignal', 'alabaster', 'altair', 'anaconda-anon-usage', 'anaconda-catalogs',
        'anaconda-client', 'anaconda-cloud-auth', 'anaconda-navigator', 'anaconda-project',
        'annotated-types', 'anyio', 'appdirs', 'archspec', 'argcomplete', 'argon2-cffi',
        'argon2-cffi-bindings', 'arrow', 'astroid', 'astropy', 'astropy-iers-data',
        'asttokens', 'astunparse', 'async-lru', 'atomicwrites', 'attrs', 'Automat',
        'autopep8', 'Babel', 'bcrypt', 'beautifulsoup4', 'binaryornot', 'black',
        'bleach', 'blinker', 'bokeh', 'boltons', 'botocore', 'Bottleneck', 'Brotli',
        'bs4', 'cachetools', 'certifi', 'cffi', 'chardet', 'charset-normalizer',
        'click', 'cloudpickle', 'colorama', 'colorcet', 'comm', 'compressed-rtf',
        'conda', 'conda-build', 'conda-content-trust', 'conda_index', 'conda-libmamba-solver',
        'conda-pack', 'conda-package-handling', 'conda_package_streaming', 'conda-repo-cli',
        'conda-token', 'constantly', 'contourpy', 'cookiecutter', 'cryptography',
        'cssselect', 'cycler', 'cytoolz', 'dask', 'dask-expr', 'dataclasses-json',
        'datashader', 'ddgs', 'debugpy', 'decorator', 'deep-translator', 'defusedxml',
        'diff-match-patch', 'dill', 'diskcache', 'distributed', 'distro', 'docstring-to-markdown',
        'docutils', 'docx2txt', 'duckduckgo_search', 'ebcdic', 'EbookLib', 'edge-tts',
        'entrypoints', 'et-xmlfile', 'executing', 'extract-msg', 'faiss-cpu', 'fastjsonschema',
        'filelock', 'flake8', 'Flask', 'flatbuffers', 'fonttools', 'fqdn', 'frozendict',
        'frozenlist', 'fsspec', 'gast', 'gitdb', 'GitPython', 'google-pasta', 'greenlet',
        'grpcio', 'gTTS', 'h11', 'h5py', 'HeapDict', 'hf-xet', 'holoviews', 'httpcore',
        'httpx', 'httpx-sse', 'huggingface-hub', 'hvplot', 'hyperlink', 'idna', 'imagecodecs',
        'imageio', 'imagesize', 'IMAPClient', 'imbalanced-learn', 'importlib-metadata',
        'incremental', 'inflection', 'iniconfig', 'intake', 'intervaltree', 'ipykernel',
        'ipython', 'ipython-genutils', 'ipywidgets', 'isoduration', 'isort', 'itemadapter',
        'itemloaders', 'itsdangerous', 'jaraco.classes', 'jedi', 'jeepney', 'jellyfish',
        'Jinja2', 'jmespath', 'joblib', 'json5', 'jsonpatch', 'jsonpointer', 'jsonschema',
        'jsonschema-specifications', 'jupyter', 'jupyter_client', 'jupyter-console',
        'jupyter_core', 'jupyter-events', 'jupyter-lsp', 'jupyter_server', 'jupyter_server_terminals',
        'jupyterlab', 'jupyterlab-pygments', 'jupyterlab_server', 'jupyterlab-widgets',
        'keras', 'keyring', 'kiwisolver', 'langchain', 'langchain-community', 'langchain-core',
        'langchain-text-splitters', 'langsmith', 'lazy_loader', 'lazy-object-proxy',
        'lckr_jupyterlab_variableinspector', 'libarchive-c', 'libmambapy', 'linkify-it-py',
        'llama_cpp_python', 'llvmlite', 'lmdb', 'locket', 'lxml', 'lz4', 'Markdown',
        'markdown-it-py', 'MarkupSafe', 'marshmallow', 'matplotlib', 'matplotlib-inline',
        'mccabe', 'mdit-py-plugins', 'mdurl', 'menuinst', 'mistune', 'mkl-fft', 'mkl-random',
        'mkl-service', 'ml_dtypes', 'more-itertools', 'mpi4py', 'mpmath', 'msgpack',
        'multidict', 'multipledispatch', 'mypy', 'mypy_extensions', 'namex', 'narwhals',
        'navigator-updater', 'nbclient', 'nbconvert', 'nbformat', 'nest-asyncio', 'networkx',
        'nltk', 'notebook', 'notebook_shim', 'numba', 'numexpr', 'numpy', 'numpydoc',
        'nvidia-cublas-cu12', 'nvidia-cuda-cupti-cu12', 'nvidia-cuda-nvrtc-cu12',
        'nvidia-cuda-runtime-cu12', 'nvidia-cudnn-cu12', 'nvidia-cufft-cu12', 'nvidia-cufile-cu12',
        'nvidia-curand-cu12', 'nvidia-cusolver-cu12', 'nvidia-cusparse-cu12', 'nvidia-cusparselt-cu12',
        'nvidia-nccl-cu12', 'nvidia-nvjitlink-cu12', 'nvidia-nvtx-cu12', 'olefile',
        'openai-whisper', 'openpyxl', 'opt-einsum', 'optree', 'orjson', 'overrides',
        'packaging', 'pandas', 'pandocfilters', 'panel', 'param', 'parsel', 'parso',
        'partd', 'pathspec', 'patsy', 'pdf2image', 'pdfminer.six', 'pexpect', 'pickleshare',
        'pillow', 'pip', 'pkce', 'pkginfo', 'platformdirs', 'plotly', 'pluggy', 'ply',
        'primp', 'prometheus-client', 'prompt-toolkit', 'propcache', 'Protego', 'protobuf',
        'psutil', 'ptyprocess', 'pure-eval', 'py-cpuinfo', 'pyarrow', 'pyasn1', 'pyasn1-modules',
        'pycodestyle', 'pycosat', 'pycparser', 'pycryptodome', 'pyct', 'pycurl', 'pydantic',
        'pydantic_core', 'pydantic-settings', 'pydeck', 'PyDispatcher', 'pydocstyle',
        'pydotplus', 'pydub', 'pyerfa', 'pyflakes', 'Pygments', 'PyJWT', 'pylint',
        'pylint-venv', 'pyls-spyder', 'pyodbc', 'pyOpenSSL', 'pyparsing', 'PyQt5',
        'PyQt5-sip', 'PyQtWebEngine', 'PySocks', 'pytesseract', 'pytest', 'python-dateutil',
        'python-dotenv', 'python-json-logger', 'python-lsp-black', 'python-lsp-jsonrpc',
        'python-lsp-server', 'python-pptx', 'python-slugify', 'python-snappy', 'pytoolconfig',
        'pyttsx3', 'pytz', 'pyviz_comms', 'PyWavelets', 'pyxdg', 'PyYAML', 'pyzmq',
        'QDarkStyle', 'qstylizer', 'QtAwesome', 'qtconsole', 'QtPy', 'queuelib', 'referencing',
        'regex', 'requests', 'requests-file', 'requests-toolbelt', 'rfc3339-validator',
        'rfc3986-validator', 'rich', 'rope', 'rpds-py', 'Rtree', 'ruamel.yaml', 'ruamel-yaml-conda',
        's3fs', 'safetensors', 'scikit-image', 'scikit-learn', 'scipy', 'Scrapy', 'seaborn',
        'SecretStorage', 'semver', 'Send2Trash', 'sentence-transformers', 'service-identity',
        'setuptools', 'sip', 'six', 'smart-open', 'smmap', 'sniffio', 'snowballstemmer',
        'sortedcontainers', 'soupsieve', 'SpeechRecognition', 'Sphinx', 'sphinxcontrib-applehelp',
        'sphinxcontrib-devhelp', 'sphinxcontrib-htmlhelp', 'sphinxcontrib-jsmath',
        'sphinxcontrib-qthelp', 'sphinxcontrib-serializinghtml', 'spyder', 'spyder-kernels',
        'SQLAlchemy', 'srt', 'stack-data', 'statsmodels', 'streamlit', 'sympy', 'tables',
        'tabulate', 'tblib', 'tenacity', 'tensorboard', 'tensorboard_data_server', 'tensorflow',
        'termcolor', 'terminado', 'text-unidecode', 'textdistance', 'textract', 'textwrap3',
        'threadpoolctl', 'three-merge', 'tifffile', 'tiktoken', 'tinycss2', 'tldextract',
        'tokenizers', 'toml', 'tomli', 'tomlkit', 'toolz', 'torch', 'tornado', 'tqdm',
        'traitlets', 'transformers', 'triton', 'truststore', 'Twisted', 'typing_extensions',
        'typing-inspect', 'typing-inspection', 'tzdata', 'tzlocal', 'uc-micro-py', 'ujson',
        'unicodedata2', 'Unidecode', 'uri-template', 'urllib3', 'w3lib', 'watchdog',
        'wcwidth', 'webcolors', 'webencodings', 'websocket-client', 'Werkzeug', 'whatthepatch',
        'wheel', 'widgetsnbextension', 'wrapt', 'wurlitzer', 'xarray', 'xlrd', 'XlsxWriter',
        'xyzservices', 'yapf', 'yarl', 'yt-dlp', 'zict', 'zipp', 'zope.interface', 'zstandard'
    ]

clima_url = "http://api.openweathermap.org/data/2.5/weather"

forecast_url = "http://api.openweathermap.org/data/2.5/forecast"

# Download Torrent constants

QB_URL = "http://192.168.1.44:8080"
QB_USER = "admin"
QB_PASSWORD = "adminadmin"
