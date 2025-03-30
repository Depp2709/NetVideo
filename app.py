from flask import Flask, render_template, request, redirect, url_for
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Folder untuk menyimpan video yang diupload
UPLOAD_FOLDER = 'static/videos'
ALLOWED_EXTENSIONS = {'mp4', 'avi', 'mov', 'mkv'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Fungsi untuk memeriksa ekstensi file video
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    # Mendapatkan daftar video yang diupload
    videos = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('index.html', videos=videos)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return redirect(url_for('index'))
    return 'File not allowed'

if __name__ == '__main__':
    app.run(debug=True)
