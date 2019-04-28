import app
import cv2
from datetime import timedelta
from flask import render_template
from flask import request
from flask import send_from_directory
import matlab.engine
import os
import time
from werkzeug.utils import secure_filename
from . import main
from . import function_design

UPLOAD_FOLDER = 'D:/program/ec500_web/app/static/images'
ALLOWED_EXTENSIONS = set(['png','jpg','jpeg'])

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.send_file_max_age_default = timedelta(seconds=1)

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
            user_input = request.form.get("name")
            upload_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(upload_path)

            img = cv2.imread(upload_path)
            cv2.imwrite(os.path.join(UPLOAD_FOLDER, 'test.jpg'), img)

            return render_template('upload_ok.html', userinput=user_input, val1=time.time())
            #return training.evaluate_one_image()
            # return vgg1999.accuracy()
            # return 'eee'
            #return one_image.accuracy()
            #return redirect(url_for('uploaded_file',filename=filename)),training.evaluate_one_image()
    return render_template("uploaded_file.html")