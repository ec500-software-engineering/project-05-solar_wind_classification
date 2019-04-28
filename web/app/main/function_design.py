import matlab.engine
import os

def classifier():
    # self.file = self.dic + '/matlab/' + filename
    matlab_classifier = matlab.engine.start_matlab()
    matlab_classifier.addpath('./main/matlab')
    print("Matlab Engine Loading... ...")
    classifier_result = matlab_classifier.classify_solar_wind(nargout=0)
    # classifier_result = matlab_classifier.classify_solar_wind(self.file)
    print("Predicting... ...",type(classifier_result))
    matlab_classifier.quit()
    prediction = open("./result.dat", "w")
    prediction.write(str(classifier_result))
    prediction.close()



classifier()

