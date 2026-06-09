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

# PYTHON CHEAT SHEET

============================================================

1. ENTRADA Y SALIDA
   ============================================================

+----------------------+--------------------------------------+-----------------------------------+
| COMANDO              | DESCRIPCIÓN                          | EJEMPLO                           |
+----------------------+--------------------------------------+-----------------------------------+
| input()              | Leer una línea                       | n = int(input())                  |
| print()              | Mostrar resultado                    | print(n)                          |
| split()              | Separar cadena                       | input().split()                   |
| map()                | Aplicar conversión                   | map(int, input().split())         |
| list()               | Convertir iterable a lista           | list(map(int, input().split()))   |
+----------------------+--------------------------------------+-----------------------------------+

============================================================
2. LISTAS
=========

+----------------------+--------------------------------------+-----------------------------------+
| COMANDO              | DESCRIPCIÓN                          | EJEMPLO                           |
+----------------------+--------------------------------------+-----------------------------------+
| append(x)            | Añadir elemento                      | l.append(5)                       |
| insert(i,x)          | Insertar en posición                 | l.insert(0,10)                    |
| remove(x)            | Eliminar valor                       | l.remove(5)                       |
| pop()                | Eliminar último                      | l.pop()                           |
| pop(i)               | Eliminar posición                    | l.pop(2)                          |
| reverse()            | Invertir lista                       | l.reverse()                       |
| sort()               | Ordenar lista                        | l.sort()                          |
| sorted()             | Ordenar sin modificar                | sorted(l)                         |
| len()                | Tamaño                               | len(l)                            |
| max()                | Mayor valor                          | max(l)                            |
| min()                | Menor valor                          | min(l)                            |
| sum()                | Suma total                           | sum(l)                            |
+----------------------+--------------------------------------+-----------------------------------+

============================================================
3. LIST COMPREHENSION
=====================

Crear lista

[x for x in range(10)]

Filtrar

[x for x in nums if x > 0]

Transformar

[x*x for x in nums]

Ejemplo:

pares = [x for x in range(20) if x % 2 == 0]

============================================================
4. STRINGS
==========

+----------------------+--------------------------------------+-----------------------------------+
| COMANDO              | DESCRIPCIÓN                          | EJEMPLO                           |
+----------------------+--------------------------------------+-----------------------------------+
| lower()              | Minúsculas                           | s.lower()                         |
| upper()              | Mayúsculas                           | s.upper()                         |
| capitalize()         | Primera letra mayúscula              | s.capitalize()                    |
| replace()            | Reemplazar texto                     | s.replace("a","b")                |
| find()               | Buscar posición                      | s.find("abc")                     |
| count()              | Contar ocurrencias                   | s.count("a")                      |
| split()              | Separar cadena                       | s.split()                         |
| join()               | Unir lista                           | "-".join(lista)                   |
| strip()              | Quitar espacios                      | s.strip()                         |
| startswith()         | Empieza por                          | s.startswith("abc")               |
| endswith()           | Termina por                          | s.endswith("xyz")                 |
+----------------------+--------------------------------------+-----------------------------------+

============================================================
5. DICCIONARIOS
===============

+----------------------+--------------------------------------+-----------------------------------+
| COMANDO              | DESCRIPCIÓN                          | EJEMPLO                           |
+----------------------+--------------------------------------+-----------------------------------+
| dict()               | Crear diccionario                    | d = {}                            |
| get()                | Obtener valor seguro                 | d.get("x",0)                      |
| keys()               | Claves                               | d.keys()                          |
| values()             | Valores                              | d.values()                        |
| items()              | Clave y valor                        | d.items()                         |
+----------------------+--------------------------------------+-----------------------------------+

Contador manual:

freq = {}

for x in lista:
freq[x] = freq.get(x,0) + 1

============================================================
6. SETS
=======

+----------------------+--------------------------------------+-----------------------------------+
| COMANDO              | DESCRIPCIÓN                          | EJEMPLO                           |
+----------------------+--------------------------------------+-----------------------------------+
| set()                | Crear conjunto                       | s = set(lista)                    |
| add()                | Añadir elemento                      | s.add(5)                          |
| remove()             | Eliminar elemento                    | s.remove(5)                       |
| union()              | Unión                                | a.union(b)                        |
| intersection()       | Intersección                         | a.intersection(b)                 |
| difference()         | Diferencia                           | a.difference(b)                   |
| symmetric_difference | Diferencia simétrica                 | a.symmetric_difference(b)         |
+----------------------+--------------------------------------+-----------------------------------+

Eliminar duplicados:

unicos = list(set(lista))

============================================================
7. FUNCIONES BUILT-IN
=====================

+----------------------+--------------------------------------+-----------------------------------+
| COMANDO              | DESCRIPCIÓN                          | EJEMPLO                           |
+----------------------+--------------------------------------+-----------------------------------+
| len()                | Tamaño                               | len(lista)                        |
| sum()                | Suma                                 | sum(lista)                        |
| min()                | Mínimo                               | min(lista)                        |
| max()                | Máximo                               | max(lista)                        |
| abs()                | Valor absoluto                       | abs(-5)                           |
| round()              | Redondear                            | round(5.67)                       |
| bin()                | Binario                              | bin(10)                           |
| oct()                | Octal                                | oct(10)                           |
| hex()                | Hexadecimal                          | hex(10)                           |
+----------------------+--------------------------------------+-----------------------------------+

============================================================
8. ENUMERATE Y ZIP
==================

enumerate()

for i, valor in enumerate(lista):
print(i, valor)

zip()

for a, b in zip(lista1, lista2):
print(a, b)

============================================================
9. LAMBDA
=========

Función anónima

lambda x: x*x

Ejemplo

cuadrado = lambda x: x*x

============================================================
10. FILTER
==========

Filtrar elementos

nums = [1,2,3,4,5]

pares = list(
filter(lambda x: x % 2 == 0, nums)
)

============================================================
11. MAP
=======

Transformar elementos

nums = [1,2,3]

cuadrados = list(
map(lambda x: x*x, nums)
)

============================================================
12. SORTED CON KEY
==================

Ordenar por columna

alumnos = [
("Ana",20),
("Luis",18)
]

sorted(alumnos, key=lambda x:x)

Orden descendente

sorted(alumnos,
key=lambda x:x,
reverse=True)

============================================================
13. ANY Y ALL
=============

Alguno cumple

any(x > 0 for x in nums)

Todos cumplen

all(x > 0 for x in nums)

============================================================
14. COLLECTIONS
===============

from collections import Counter

Contar elementos

Counter("AAABBC")

Resultado

{
'A':3,
'B':2,
'C':1
}

============================================================
15. ITERTOOLS
=============

from itertools import product
from itertools import permutations
from itertools import combinations

Producto cartesiano

product(A,B)

Permutaciones

permutations("ABC",2)

Combinaciones

combinations("ABC",2)

============================================================
16. REGEX
=========

import re

+----------------------+--------------------------------------+-----------------------------------+
| COMANDO              | DESCRIPCIÓN                          | EJEMPLO                           |
+----------------------+--------------------------------------+-----------------------------------+
| re.match()           | Coincide desde inicio                | re.match(p,s)                     |
| re.search()          | Buscar patrón                        | re.search(p,s)                    |
| re.findall()         | Todas las coincidencias              | re.findall(p,s)                   |
| re.sub()             | Sustituir patrón                     | re.sub(p,r,s)                     |
+----------------------+--------------------------------------+-----------------------------------+

Patrones más usados

\d      número
\D      no número
\w      letra o número
\s      espacio
^       inicio
$       final

* ```
    uno o más
  ```

- ```
    cero o más
  ```

?       opcional
{n}     exactamente n

Email válido

r'^[\w-]+@[A-Za-z0-9]+.[A-Za-z]{1,3}$'

============================================================
17. EXCEPCIONES
===============

try:
x = int(input())
except ValueError:
print("Error")

============================================================
18. NUMPY
=========

import numpy as np

Crear array

np.array([1,2,3])

Cambiar forma

arr.reshape(2,2)

Transponer

arr.transpose()

Aplanar

arr.flatten()

Media

np.mean(arr)

Varianza

np.var(arr)

Desviación típica

np.std(arr)

============================================================
19. TOP 20 COMANDOS MÁS USADOS EN HACKERRANK
============================================

input()
print()
split()
map()
list()
set()
dict()
append()
sort()
sorted()
len()
sum()
max()
min()
enumerate()
zip()
lambda
filter()
Counter()
re.match()

============================================================
20. PLANTILLA BASE PARA EL 80% DE PROBLEMAS
===========================================

n = int(input())

arr = list(
map(int, input().split())
)

resultado = ...

print(resultado)



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

HACKERRANK 10 DAYS OF JAVASCRIPT - COMMAND REFERENCE

====================================================================================================
| Exercise                          | Command / Feature           | Explanation                   |
====================================================================================================
| Day 0 - Hello World               | console.log()              | Prints output to the console. |
| Example                           | console.log("Hello, World!");
----------------------------------------------------------------------------------------------------
| Day 0 - Data Types                | Number(), String(), +      | Converts and combines values. |
| Example                           | let sum = Number(4) + 4;
----------------------------------------------------------------------------------------------------
| Day 1 - Arithmetic Operators      | +, -, *, /                | Basic arithmetic operations.  |
| Example                           | let area = length * width;
----------------------------------------------------------------------------------------------------
| Day 1 - Functions                 | function                  | Defines reusable code blocks. |
| Example                           | function factorial(n){ return n; }
----------------------------------------------------------------------------------------------------
| Day 1 - Let and Const             | let, const                | Block-scoped variables.       |
| Example                           | const PI = 3.14; let r = 2;
----------------------------------------------------------------------------------------------------
| Day 2 - If-Else                   | if, else if, else         | Conditional execution.        |
| Example                           | if(score > 25){ grade="A"; }
----------------------------------------------------------------------------------------------------
| Day 2 - Switch                    | switch                    | Handles multiple conditions.  |
| Example                           | switch(day){ case 1: break; }
----------------------------------------------------------------------------------------------------
| Day 2 - Loops                     | for, while                | Repeats code execution.       |
| Example                           | for(let i=0;i<5;i++){ console.log(i); }
----------------------------------------------------------------------------------------------------
| Day 3 - Arrays                    | [], length, index         | Stores collections of values. |
| Example                           | let nums=[1,2,3]; nums[0];
----------------------------------------------------------------------------------------------------
| Day 3 - Try/Catch                 | try, catch, finally       | Handles runtime errors.       |
| Example                           | try{ x(); } catch(err){ console.log(err); }
----------------------------------------------------------------------------------------------------
| Day 3 - Throw                     | throw                     | Creates custom exceptions.    |
| Example                           | throw new Error("Invalid");
----------------------------------------------------------------------------------------------------
| Day 4 - Rectangle Object          | Object Literal            | Creates structured objects.   |
| Example                           | let rect={length:4,width:5};
----------------------------------------------------------------------------------------------------
| Day 4 - Count Objects             | filter()                  | Filters array elements.       |
| Example                           | arr.filter(x => x.x === x.y);
----------------------------------------------------------------------------------------------------
| Day 4 - Classes                   | class, constructor        | Creates object blueprints.    |
| Example                           | class Polygon{ constructor(sides){} }
----------------------------------------------------------------------------------------------------
| Day 5 - Inheritance               | extends, super()          | Inherits from parent classes. |
| Example                           | class Dog extends Animal{ super(); }
----------------------------------------------------------------------------------------------------
| Day 5 - Template Literals         | `${}`                     | Embeds values in strings.     |
| Example                           | `Hello ${name}`
----------------------------------------------------------------------------------------------------
| Day 5 - Arrow Functions           | =>                        | Short function syntax.        |
| Example                           | const square = x => x*x;
----------------------------------------------------------------------------------------------------
| Day 6 - Bitwise Operators         | &, |, ^, <<, >>          | Binary operations.            |
| Example                           | let result = a & b;
----------------------------------------------------------------------------------------------------
| Day 6 - JavaScript Dates          | Date                      | Works with dates and times.   |
| Example                           | let d = new Date();
----------------------------------------------------------------------------------------------------
| Day 7 - Regex I                   | RegExp, test()            | Pattern matching.             |
| Example                           | /^[aeiou].*[aeiou]$/
----------------------------------------------------------------------------------------------------
| Day 7 - Regex II                  | Character Classes         | Matches character groups.     |
| Example                           | /[a-zA-Z]/
----------------------------------------------------------------------------------------------------
| Day 7 - Regex III                 | Quantifiers               | Controls repetitions.         |
| Example                           | /\d{3,}/
----------------------------------------------------------------------------------------------------
| Day 8 - Create a Button           | createElement()           | Creates HTML elements.        |
| Example                           | document.createElement("button");
----------------------------------------------------------------------------------------------------
| Day 8 - Create a Button           | addEventListener()        | Handles user events.          |
| Example                           | btn.addEventListener("click", fn);
----------------------------------------------------------------------------------------------------
| Day 8 - Buttons Container         | DOM Manipulation          | Updates page content.         |
| Example                           | document.getElementById("btn").innerHTML++;
----------------------------------------------------------------------------------------------------
| Day 9 - Binary Calculator         | parseInt(), toString()    | Binary/decimal conversion.    |
| Example                           | parseInt("101",2);
----------------------------------------------------------------------------------------------------
| Day 9 - Binary Calculator         | eval()                    | Evaluates expressions.        |
| Example                           | eval("1+2");
====================================================================================================

MOST IMPORTANT JAVASCRIPT COMMANDS

console.log()          -> Print output to console
let                    -> Declare block-scoped variable
const                  -> Declare constant variable
var                    -> Declare function-scoped variable
function               -> Create a function
return                 -> Return a value from a function
if / else              -> Conditional execution
switch                 -> Multiple condition selection
for                    -> Loop through iterations
while                  -> Loop while condition is true
[]                     -> Create arrays
.length                -> Get array/string length
.map()                 -> Transform array elements
.filter()              -> Filter array elements
.reduce()              -> Reduce array to a single value
{}                     -> Create objects
class                  -> Define classes
constructor            -> Initialize class objects
extends                -> Inherit from another class
super()                -> Call parent constructor
try / catch            -> Handle exceptions
throw                  -> Raise exceptions
Date                   -> Work with dates
RegExp                 -> Regular expressions
test()                 -> Test regex matches
createElement()        -> Create DOM elements
getElementById()       -> Select DOM elements
addEventListener()     -> Listen for events
parseInt()             -> Convert string to integer
toString()             -> Convert value to string
& | ^ << >>            -> Bitwise operators
=>                     -> Arrow function syntax
`${}`                  -> Template literals

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

Basic Select

| Comando / Ejercicio          | Descripción                                     | Snippet                                                                  |
| ---------------------------- | ----------------------------------------------- | ------------------------------------------------------------------------ |
| Revising the Select Query I  | Ciudades USA con población > 100000             | `SELECT * FROM CITY WHERE COUNTRYCODE='USA' AND POPULATION > 100000;`    |
| Revising the Select Query II | Nombres de ciudades USA con población > 120000  | `SELECT NAME FROM CITY WHERE COUNTRYCODE='USA' AND POPULATION > 120000;` |
| Select All                   | Devuelve todas las filas                        | `SELECT * FROM CITY;`                                                    |
| Select By ID                 | Busca ciudad por ID                             | `SELECT * FROM CITY WHERE ID=1661;`                                      |
| Japanese Cities' Attributes  | Todas las ciudades de Japón                     | `SELECT * FROM CITY WHERE COUNTRYCODE='JPN';`                            |
| Japanese Cities' Names       | Nombre de ciudades japonesas                    | `SELECT NAME FROM CITY WHERE COUNTRYCODE='JPN';`                         |
| Employee Salaries            | Empleados con salario >2000 y menos de 10 meses | `SELECT NAME FROM EMPLOYEE WHERE SALARY>2000 AND MONTHS<10;`             |
| Higher Than 75 Marks         | Estudiantes con nota >75                        | `SELECT NAME FROM STUDENTS WHERE MARKS>75;`                              |

Weather Observation Station

| Ejercicio  | Descripción                         | Snippet                                           |
| ---------- | ----------------------------------- | ------------------------------------------------- |
| Station 1  | Ciudad y estado                     | `SELECT CITY, STATE FROM STATION;`                |
| Station 3  | Ciudades únicas con ID par          | `SELECT DISTINCT CITY FROM STATION WHERE ID%2=0;` |
| Station 4  | Diferencia entre total y únicos     | `SELECT COUNT(CITY)-COUNT(DISTINCT CITY);`        |
| Station 5  | Ciudad más corta y más larga        | `ORDER BY LENGTH(CITY)`                           |
| Station 6  | Empiezan por vocal                  | `WHERE CITY REGEXP '^[AEIOU]'`                    |
| Station 7  | Terminan por vocal                  | `WHERE CITY REGEXP '[AEIOU]$'`                    |
| Station 8  | Empiezan y terminan por vocal       | `WHERE CITY REGEXP '^[AEIOU].*[AEIOU]$'`          |
| Station 9  | No empiezan por vocal               | `WHERE CITY NOT REGEXP '^[AEIOU]'`                |
| Station 10 | No terminan por vocal               | `WHERE CITY NOT REGEXP '[AEIOU]$'`                |
| Station 11 | No empiezan o no terminan por vocal | `NOT REGEXP`                                      |
| Station 12 | No empiezan ni terminan por vocal   | `NOT REGEXP '^[AEIOU].*[AEIOU]$'`                 |
| Station 13 | Suma de LAT_N en rango              | `SUM(LAT_N)`                                      |
| Station 14 | Máximo LAT_N menor que valor        | `MAX(LAT_N)`                                      |
| Station 15 | LONG_W asociado a LAT_N máximo      | Subconsulta                                       |
| Station 16 | LAT_N mínimo superior a valor       | `MIN(LAT_N)`                                      |
| Station 17 | LONG_W asociado a LAT_N mínimo      | Subconsulta                                       |
| Station 18 | Distancia Manhattan                 | `ABS(MAX(LAT)-MIN(LAT))+ABS(MAX(LONG)-MIN(LONG))` |
| Station 19 | Distancia Euclídea                  | `SQRT(POW(...))`                                  |
| Station 20 | Mediana                             | `ROW_NUMBER()`                                    |


Aggregation

| Ejercicio                            | Descripción                        | Snippet                  |
| ------------------------------------ | ---------------------------------- | ------------------------ |
| Revising Aggregations Count Function | Cuenta ciudades >100000 habitantes | `SELECT COUNT(*)`        |
| Revising Aggregations Sum Function   | Suma población California          | `SELECT SUM(POPULATION)` |
| Revising Aggregations Average        | Promedio población California      | `SELECT AVG(POPULATION)` |
| Average Population                   | Promedio mundial                   | `SELECT AVG(POPULATION)` |
| Japan Population                     | Población total Japón              | `SELECT SUM(POPULATION)` |
| Population Density Difference        | Diferencia entre máximo y mínimo   | `MAX()-MIN()`            |
| Top Earners                          | Salario máximo generado            | `SALARY*MONTHS`          |


Advanced Select

| Ejercicio         | Descripción                 | Snippet                                   |
| ----------------- | --------------------------- | ----------------------------------------- |
| Type of Triangle  | Clasificación de triángulos | `CASE WHEN ... THEN ... END`              |
| The PADS          | Formato Nombre(Ocupación)   | `CONCAT(NAME,'(',LEFT(OCCUPATION,1),')')` |
| Occupations       | Pivotar ocupaciones         | `ROW_NUMBER() OVER()`                     |
| Binary Tree Nodes | Root, Inner, Leaf           | `CASE WHEN P IS NULL THEN 'Root' ...`     |
| New Companies     | Conteos jerárquicos         | `COUNT(DISTINCT ...)`                     |


Basic Join

| Ejercicio                            | Descripción             | Snippet                |
| ------------------------------------ | ----------------------- | ---------------------- |
| African Cities                       | Ciudades africanas      | `JOIN COUNTRY ON ...`  |
| Average Population of Each Continent | Promedio por continente | `GROUP BY CONTINENT`   |
| Population Census                    | Suma población Asia     | `JOIN + SUM()`         |
| The Report                           | Notas y estudiantes     | `JOIN STUDENTS GRADES` |


Advanced Join

| Ejercicio            | Descripción                        | Snippet                 |
| -------------------- | ---------------------------------- | ----------------------- |
| Challenges           | Hackers con máximo número de retos | `GROUP BY HACKER_ID`    |
| Contest Leaderboard  | Mejor puntuación por reto          | `MAX(SCORE)`            |
| SQL Project Planning | Agrupar proyectos consecutivos     | `LEAD()`                |
| Placements           | Comparación salarial               | `JOIN FRIENDS PACKAGES` |


Parte B — Chuleta SQL de Comandos

| Comando      | Descripción                | Ejemplo                                   |
| ------------ | -------------------------- | ----------------------------------------- |
| SELECT       | Seleccionar columnas       | `SELECT name FROM employee;`              |
| DISTINCT     | Eliminar duplicados        | `SELECT DISTINCT city FROM station;`      |
| WHERE        | Filtrar registros          | `WHERE population > 100000`               |
| ORDER BY     | Ordenar resultados         | `ORDER BY salary DESC`                    |
| LIMIT        | Limitar filas              | `LIMIT 10`                                |
| GROUP BY     | Agrupar datos              | `GROUP BY department`                     |
| HAVING       | Filtrar grupos             | `HAVING COUNT(*) > 5`                     |
| COUNT()      | Contar registros           | `COUNT(*)`                                |
| SUM()        | Sumar valores              | `SUM(salary)`                             |
| AVG()        | Promedio                   | `AVG(salary)`                             |
| MAX()        | Máximo                     | `MAX(salary)`                             |
| MIN()        | Mínimo                     | `MIN(salary)`                             |
| ROUND()      | Redondear                  | `ROUND(avg_salary,2)`                     |
| CONCAT()     | Concatenar texto           | `CONCAT(name,'(',role,')')`               |
| CASE         | Condicional SQL            | `CASE WHEN salary>5000 THEN 'Senior' END` |
| INNER JOIN   | Unión interna              | `JOIN dept ON emp.dept_id=dept.id`        |
| LEFT JOIN    | Mantiene tabla izquierda   | `LEFT JOIN orders`                        |
| RIGHT JOIN   | Mantiene tabla derecha     | `RIGHT JOIN orders`                       |
| UNION        | Une resultados             | `SELECT ... UNION SELECT ...`             |
| UNION ALL    | Une manteniendo duplicados | `UNION ALL`                               |
| EXISTS       | Verifica existencia        | `WHERE EXISTS (...)`                      |
| IN           | Lista de valores           | `WHERE city IN ('Madrid','Paris')`        |
| BETWEEN      | Rango                      | `WHERE salary BETWEEN 1000 AND 5000`      |
| LIKE         | Búsqueda por patrón        | `WHERE name LIKE 'A%'`                    |
| REGEXP       | Expresiones regulares      | `WHERE city REGEXP '^[AEIOU]'`            |
| ROW_NUMBER() | Numeración secuencial      | `ROW_NUMBER() OVER(ORDER BY salary)`      |
| RANK()       | Ranking con empates        | `RANK() OVER()`                           |
| DENSE_RANK() | Ranking continuo           | `DENSE_RANK() OVER()`                     |
| LEAD()       | Siguiente fila             | `LEAD(salary)`                            |
| LAG()        | Fila anterior              | `LAG(salary)`                             |
| CTE (WITH)   | Tabla temporal             | `WITH cte AS (...) SELECT * FROM cte;`    |
| Subquery     | Consulta anidada           | `WHERE salary > (SELECT AVG(...))`        |

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
