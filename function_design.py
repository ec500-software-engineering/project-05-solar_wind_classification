import matlab.engine
import os


class SolarWindClassifier:
    def __init__(self):
        self.dic = os.getcwd()

    def classifier(self, filename):
        self.file = self.dic + '/matlab/' + filename
        matlab_classifier = matlab.engine.start_matlab('-novm')
        print("Matlab Engine Loading... ...")
        classifier_result = matlab_classifier.classify_solar_wind('omni2_2017.dat')
        print("Predicting... ...")
        # print(classifier_result)
        matlab_classifier.quit()
        prediction = open("./result.txt", "w")
        prediction.write(str(classifier_result))
        prediction.close()


S = SolarWindClassifier()
S.classifier("omni2_2017.dat")