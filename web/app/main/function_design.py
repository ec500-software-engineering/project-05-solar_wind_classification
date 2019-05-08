import matlab.engine
import numpy as np
import scipy.io as sio

def classifier(test):
    # self.file = self.dic + '/matlab/' + filename
    save_fn = 'test.mat'
    save_array = np.array(test)
    sio.savemat(save_fn, {'array': save_array})

    matlab_classifier = matlab.engine.start_matlab()
    matlab_classifier.addpath('D:/program/ec500_web/app/main')
    print("Matlab Engine Loading... ...")
    classifier_result = matlab_classifier.classify_solar_wind(nargout=0)
    print(classifier_result)
    a = classifier_result.index(max(classifier_result))
    # classifier_result = matlab_classifier.classify_solar_wind(self.file)
    print("Predicting... ...")
    result = ['Ejecta', 'Coronal holes origin', 'Sector reversal origin', 'Streamer belts origin']
    print(result[a])
    final = result[a]
    matlab_classifier.quit()
    # prediction = open("./result.dat", "w")
    # prediction.write(str(classifier_result))
    # prediction.close()

    return classifier_result, final

classifier()

