import app
from flask import render_template
from flask import request
from flask import send_from_directory
import os
from werkzeug.utils import secure_filename
from . import main

UPLOAD_FOLDER = '/Users/y/web/uploads'
ALLOWED_EXTENSIONS = set(['png','jpg','jpeg'])

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@main.route('/upload', methods=['GET', 'POST'])
def uploaded_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            #return training.evaluate_one_image()
            # return vgg1999.accuracy()
            # return 'eee'
            #return one_image.accuracy()
            #return redirect(url_for('uploaded_file',filename=filename)),training.evaluate_one_image()
    return render_template("uploaded_file.html")