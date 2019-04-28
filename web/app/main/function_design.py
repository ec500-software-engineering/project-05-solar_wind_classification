import matlab.engine
import os


class SolarWindClassifier:
    def __init__(self):
        self.dic = os.getcwd()

    def classifier(self, filename):
        self.file = self.dic + '/matlab/' + filename
        matlab_classifier = matlab.engine.start_matlab('-novm')
        print("Matlab Engine Loading... ...")
        classifier_result = matlab_classifier.classify_solar_wind(self.file)
        print("Predicting... ...")
        matlab_classifier.quit()
        prediction = open("./result.dat", "w")
        prediction.write(classifier_result)
        prediction.close()


S = SolarWindClassifier()
S.classifier("/matlab/omni2_2017.dat")