# Flask Http Server  (Multimedia conversor http server) 
# ----------------------------------------------------------------------------------------------------------------------
# Purpose : Assist pda manue and interact as an interface in between Linux OS and Android or other OS devices via browser
# ----------------------------------------------------------------------------------------------------------------------
# Author : Manuel Portero Leiva 
# ----------------------------------------------------------------------------------------------------------------------

from flask import Flask, request, render_template, send_from_directory, send_file
from constants import INPUT_DIR, OUTPUT_DIR
import os, io, zipfile



def chatbot_http_server():

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    app = Flask(__name__)
    app.config['OUTPUT_DIR'] = OUTPUT_DIR

    @app.route('/', methods=['GET', 'POST'])
    def index():
        if request.method == 'POST':
            f = request.files['file']
            if f:
                f.save(os.path.join(app.config['OUTPUT_DIR'], f.filename))
        
        files = os.listdir(app.config['OUTPUT_DIR'])
        return render_template("index.html", files=files)

    @app.route('/files/<path:filename>')
    def download_file(filename):
        return send_from_directory(app.config['OUTPUT_DIR'], filename, as_attachment=True)

    @app.route('/download_all')
    def download_all():
        """Descarga todos los archivos del OUTPUT_DIR comprimidos en un ZIP."""
        memory_file = io.BytesIO()
        with zipfile.ZipFile(memory_file, 'w', zipfile.ZIP_DEFLATED) as zf:
            for filename in os.listdir(app.config['OUTPUT_DIR']):
                filepath = os.path.join(app.config['OUTPUT_DIR'], filename)
                if os.path.isfile(filepath):
                    zf.write(filepath, arcname=filename)
        memory_file.seek(0)
        return send_file(
            memory_file,
            as_attachment=True,
            download_name='all_files.zip',
            mimetype='application/zip'
        )    
    app.run(host='0.0.0.0', port=8080)




    
