# ENGLISH

# 🌊 Marea Chatbot v1.1.0

### 🧠 Multipurpose chatbot combining SLM, RAG and Python code actions  
---

## 📘 Overview

**Marea Chatbot** is a multipurpose virtual assistant designed to automate daily and repetitive tasks by combining:
- **SLM (Small Language Model)** for conversational interaction,
- **RAG (Retrieval-Augmented Generation)** for intelligent data retrieval,
- **Python automation** for system operations, file management, software installation, backup creation, and more.

The project is modular, with each component providing a specific set of features accessible through an interactive command-line menu.

---

## 👤 Author

**Author:** Manuel Portero Leiva  
**Version:** 1.1.0  
**Language:** Python 3.x

---

## ⚙️ Main Features

When executed, the main program displays a console-based menu allowing users to select among various operations.  
Below is an explanation of each available option:

---

### ⚙️ Option 0 — System Information
Executes the `system_information` module to display system details such as:
- CPU, RAM, OS, and storage info.
- Useful for quick diagnostics and performance monitoring.

---

### 📜 Option 1 — File Movements
Runs the `files_movements` module to perform file-related actions:
- Copy, move, rename, or delete files and folders.
- Ideal for automating file system organization.

---

### ⚙️ Option 2 — Software Installer / File Structure Setup
Executes the `software_installator` module, allowing:
- Automated installation of software packages or dependencies.
- Creation of pre-defined folder structures.
- Useful for setting up new environments or project directories.

---

### 🧰 Option 3 — Backup / USB Flash / ISO Creation
Runs the `backup_flash_isos` module to manage backup and storage media operations:
- Create system or folder backups.
- Build ISO images or prepare bootable USB drives.

---

### 💬 Option 4 — Free Conversation with AI
Triggers `initialize_gen_ai_chatbot`, launching an interactive chatbot using SLM/RAG technology:
- Enables general or technical conversations with an AI assistant.
- May require sufficient system resources if running a local model.

> 💡 The user is prompted to confirm before starting the chatbot in free conversation mode.

---

### 🎧 Option 5 — Multimedia AI Converter
Executes the `multimedia_conversor` module for intelligent multimedia transformations:
- Convert between audio, text, and image formats.
- Includes transcription or AI-based voice generation.

---

### 🔍 Option 6 — Data Search via API
Runs `api_information_search`, a panel for querying data from APIs:
- Retrieves information from predefined APIs or web endpoints.
- Useful for quick IT queries, research, or real-time information retrieval.

---

### 🚀 Option 7 — Quick Command Console and Notes
Executes `quick_notes_command_console`, an interactive command-line assistant:
- Run terminal commands quickly.
- Store short notes or reminders.
- Great for developers or IT technicians needing a lightweight command console.

---

### ❌ Option 8 — Exit
Ends the program and displays a friendly goodbye message.

---

## 🔁 Execution Flow

1. The program runs inside a `while True` loop until the user chooses to exit.  
2. After each operation, the user is asked whether to continue or quit.  
3. Exception handling ensures stability and prevents crashes.  
4. The screen is cleared each cycle using `os.system("clear")` for a clean UI.

---

## 🧩 Project Structure




# -------------------------------------------------------------------------------------------------------------------------------------------------------

# ESPAÑOL

# 🌊 Marea Chatbot v1.1.0

### 🧠 Multipurpose chatbot combining SLM, RAG and Python code actions  
---

## 📘 Descripción general

**Marea Chatbot** es un asistente virtual multipropósito diseñado para automatizar tareas diarias y repetitivas mediante una combinación de:
- **SLM (Small Language Model)** para interacción conversacional,
- **RAG (Retrieval-Augmented Generation)** para búsquedas y consultas inteligentes,
- **acciones Python** para control del sistema, gestión de archivos, instalación de software, creación de backups, y más.

El proyecto está estructurado en módulos que permiten ejecutar diferentes funcionalidades desde un menú interactivo en consola.

---

## 👤 Autor

**Autor:** Manuel Portero Leiva  
**Versión:** 1.1.0  
**Lenguaje:** Python 3.x

---

## ⚙️ Funcionalidades principales

Al ejecutar el programa principal, el usuario es recibido con un menú en consola donde puede elegir entre distintas operaciones.  
A continuación, se describe cada opción disponible:

---

### ⚙️ Opción 0 — Información del sistema
Ejecuta el módulo `system_information` que muestra información técnica del equipo:
- CPU, RAM, sistema operativo y almacenamiento.
- Ideal para diagnósticos rápidos o monitorización básica.

---

### 📜 Opción 1 — Movimientos de archivos
Ejecuta el módulo `files_movements` para realizar operaciones de archivos:
- Copiar, mover, renombrar o eliminar archivos y carpetas.
- Permite automatizar la organización del sistema de archivos.

---

### ⚙️ Opción 2 — Instalador de software / estructuras de archivos
Ejecuta el módulo `software_installator` que facilita:
- Instalación automática de paquetes o dependencias.
- Creación de estructuras de carpetas personalizadas.
- Ideal para preparar entornos de trabajo o despliegue rápido.

---

### 🧰 Opción 3 — Generación de backups / USB flash / ISOs
Ejecuta el módulo `backup_flash_isos` para gestionar copias de seguridad y medios extraíbles:
- Crear backups locales o en dispositivos externos.
- Generar imágenes ISO o preparar unidades USB de arranque.

---

### 💬 Opción 4 — Conversación libre con IA
Ejecuta `initialize_gen_ai_chatbot`, un modo de conversación libre con un modelo de lenguaje (SLM/RAG):
- Posibilita charlas interactivas o consultas técnicas.
- Requiere buena capacidad del sistema si se ejecuta un modelo local.

> 💡 Antes de iniciar, el usuario debe confirmar si desea ejecutar el chatbot en modo libre.

---

### 🎧 Opción 5 — Conversor multimedia por IA
Ejecuta el módulo `multimedia_conversor` para transformar archivos multimedia mediante IA:
- Conversión entre audio, texto, e imagen.
- Puede incluir transcripción o generación de voz mediante modelos IA.

---

### 🔍 Opción 6 — Buscador de datos vía API
Ejecuta `api_information_search`, un panel de búsqueda y consulta externa:
- Obtiene información desde APIs predefinidas o de internet.
- Ideal para búsquedas rápidas, consultas IT o acceso a bases de datos en línea.

---

### 🚀 Opción 7 — Consola de comandos rápidos y notas
Ejecuta `quick_notes_command_console`, una pequeña terminal interactiva:
- Permite ejecutar comandos rápidos.
- Ofrece una libreta para guardar notas o recordatorios técnicos.
- Útil para técnicos IT y desarrolladores.

---

### ❌ Opción 8 — Salir
Finaliza el programa mostrando un mensaje de despedida.

---

## 🔁 Flujo de ejecución

1. El programa se ejecuta en bucle (`while True`) hasta que el usuario decida salir.  
2. Tras cada acción, se pregunta si desea continuar o finalizar.  
3. Se implementa manejo de excepciones en cada módulo para evitar errores de ejecución.  
4. La pantalla se limpia en cada ciclo (`os.system("clear")`) para mantener la interfaz limpia.

---

## 🧩 Estructura de módulos principales

