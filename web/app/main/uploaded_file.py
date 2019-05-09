import app
import cv2
from datetime import timedelta
from flask import render_template
from flask import request,redirect,flash,url_for
from flask import send_from_directory
import matlab.engine
import numpy as np
import scipy.io as sio
import os
import time
from werkzeug.utils import secure_filename
from . import main
from .forms import SigninForm

UPLOAD_FOLDER = 'D:/program/ec500_web/app/static/images'
ALLOWED_EXTENSIONS = set(['png','jpg','jpeg'])

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.send_file_max_age_default = timedelta(seconds=1)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

def classifier(test):
    # self.file = self.dic + '/matlab/' + filename
    save_fn = 'D:/program/ec500_web/app/main/test.mat'
    # print(type(test))
    save_array = np.array(test)
    # print(type(save_array))
    sio.savemat(save_fn, {'array': save_array})

    matlab_classifier = matlab.engine.start_matlab()
    matlab_classifier.addpath('D:/program/ec500_web/app/main')
    print("Matlab Engine Loading... ...")
    matlab_classifier.classify_solar_wind(nargout=0)
    classifier_result = sio.loadmat('D:/program/ec500_web/app/main/result.mat')
    # print(type(classifier_result['result']))
    classfier_reg = classifier_result.get('result').tolist()
    # print('........11......')
    reg_tmp = [0.0 for n in range(4)]
    for i in range(4):
        reg_tmp[i] = classfier_reg[0][i]
    a = reg_tmp.index(max(reg_tmp))
    print("Predicting... ...")
    result = ['Ejecta', 'Coronal holes origin', 'Sector reversal origin', 'Streamer belts origin']
    print(result[a])
    final = result[a]
    matlab_classifier.quit()
    # prediction = open("./result.dat", "w")
    # prediction.write(str(classifier_result))
    # prediction.close()
    # classifier_result = [0.16873966610018898,0.45647390200467747,0.13808129897583565,0.23670513291929793]
    # final = 'Ejecta'
    return reg_tmp , final

@main.route('/upload', methods=['GET', 'POST'])
def uploaded_file():

    signin_form = SigninForm(request.form)
    if request.method == 'POST':
        if signin_form.username.data == 'Mingdao': #and signin_form.validate()
            print(".....................")
            username2 = signin_form.username2.data
            username3 = signin_form.username3.data
            username4 = signin_form.username4.data
            username5 = signin_form.username5.data
            username6 = signin_form.username6.data
            username7 = signin_form.username7.data
            username8 = signin_form.username8.data
            input_array = [float(username2),float(username3),float(username4),float(username5),float(username6),float(username7),float(username8)]
            print('calculating...........')
            # print(type(input_array[0]))
            pred, final = classifier(input_array)
            # print(type(pred))
            return render_template('upload_ok.html',val1=time.time(),
                                   signin_form = signin_form,pred1=pred[0],
                                   pred2=pred[1],pred3=pred[2],pred4=pred[3]
                                   ,final=final) #,final=final

    # if request.method == 'POST':
    #     if(request.files['file']):
    #         file = request.files['file']
    #         if file and allowed_file(file.filename):
    #             filename = secure_filename(file.filename)
    #             # user_input = request.form.get("name")
    #             # user_input2 = request.form.get("2")
    #             # user_input3 = request.form.get("3")
    #             # user_input4 = request.form.get("4")
    #             # user_input5 = request.form.get("5")
    #             # user_input6 = request.form.get("6")
    #             # user_input7 = request.form.get("7")
    #             upload_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    #             file.save(upload_path)
    #             print(upload_path)
    #             print('calculating...........')
    #             pred = classifier()
    #             # print(os.system("python D:/program/ec500_web/app/main/function_design.py"))
    #
    #             img = cv2.imread(upload_path)
    #             cv2.imwrite(os.path.join(UPLOAD_FOLDER, 'test.jpg'), img)
    #
    #         return render_template('upload_ok.html',signin_form=signin_form,
    #                                val1=time.time())

    return render_template("uploaded_file.html", signin_form=signin_form)

