![image](https://travis-ci.org/ec500-software-engineering/project-05-solar_wind_classification.svg?branch=master)
# Solar_Wind_Classification_No.1
This is a final projcet for EC500 Software Engineering

## User Story:
The main users of this classification are astronomers and geographers.<br>
For the astronomers, they can observe and detect the solar wind to do research. Analyzing and classifying the solar wind can help professors learn more about the son and fixed stars. Every data will be stored in a database, which will record the behavior of the son to analyze it thoroughly.<br>

For the geographers, they can do some prediction on the earth electromagnetic field movement according to the classification of the solar wind. They can observe and learn how the solar wind influence the earth.<br>


## Technology:
We present a four-category classification algorithm for the solar wind, based on Gaussian Process. The four categories are: ejecta, coronal hole origin plasma, streamer belt origin plasma, and sector reversal origin plasma. The algorithm is trained and tested on a labeled portion of the OMNI data set which will be updated per day till now.The raw data is with 7 features which are **Solar wind speed(Vsw)**,
**Proton temperature standard deviation(𝜎T)**, **Sunspot number(R)**, **Solar radio flux((10.7 cm) F10.7)**, **Alfven speed(vA)**, **Proton specific entropy(Sp)**, **and Temperature ratio(Texp∕Tp)**.<br>
For these data, we plan to use Guassian process classification method.GP is a nonparametric statistical model, which has the advantage of producing probabilistic results, employing a Bayesian approach. This is a key feature that makes GP models different from most machine learning schemes. In particular, other classification schemes have the goal of finding the category boundaries in a multidimensional input space, unambiguously partitioning the input space into categories. The probabilistic approach is more flexible and informative, because it attaches a confidence level to predictions.<br>

## Modules to be chosen:
1.	Dataset: gather data from the OMNI and do the initial process on it.<br>
2.	Algorithm: Gaussian regression.<br>
3.	Learning model: Matlab(from the reference)/Tensorflow(Python)<br>
4.	Prediction evaluation: Based on the record in the OMNI database to calculate the accuracy of the classifier.<br>

## Sprint 1 goal:
The first sprint is an open stage of the project. During the first sprint, we plan to achieve four goals.<br>
1.	Learn the paper in the project reference link. Know the structure of this project and the basic algorithm.<br>
2.	Do a specific plan on how to achieve all the functions of the project.<br>
3.	Construct the basic structure of solar wind classification.<br>
4.	Think a way of a direction on how to optimize the project structure or algorithm.<br>

## Environemts and APIs:
Matlab<br>

## Architecture:
![image](https://github.com/ec500-software-engineering/project-05-solar_wind_classification/blob/master/images/Blank%20Diagram.png) 

## Usage:
Download all the files in the directory 'Matlab', then follow the instruction in the classify_solar_wind.m. The prediction of the classifer is stored in the trained.mat.


## Authors:

* **Jing Li** - jingli18@bu.edu - *Initial work*
* **Mingdao Che** - mdche@bu.edu - *Initial work*

## Citing literature:
[Classification of Solar Wind With Machine Learning Enrico Camporeale  Algo Carè  Joseph E. Borovsky First published: 16 October 2017](https://agupubs.onlinelibrary.wiley.com/doi/abs/10.1002/2017JA024383)
