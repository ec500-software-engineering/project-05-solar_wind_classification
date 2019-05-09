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

## Environemts and APIs(Partial):
All of the related librarise included in requirements.txt<br>
Matlab<br>
Flask==1.0.2<br>>
matlabengineforpython===R2018a<br>
numpy==1.16.3<br>
opencv-python==4.1.0.25<br>
scipy==1.2.1<br>
SQLAlchemy==1.3.3<br>
WTForms==2.2.1<br>


## Architecture:
![image](https://github.com/ec500-software-engineering/project-05-solar_wind_classification/blob/master/images/Blank%20Diagram.png) 

## Usage:
1) Download all the files in the repo and setup related libraries on your computer or virtual machine. <br>
2) cd to the loacation where you dowloaede the project and then type python manage.py runserver. <br>
3) Open the website on your chrome, the address may be http://127.0.0.1:5000/ <br>

## Some view of our website:
### Home
![image](https://github.com/ec500-software-engineering/project-05-solar_wind_classification/blob/master/web/images_readme/127.0.0.1_5000_.png)

### Upload file
![image](https://github.com/ec500-software-engineering/project-05-solar_wind_classification/blob/master/web/images_readme/127.0.0.1_5000_upload.png)

### Upload log
![image](https://github.com/ec500-software-engineering/project-05-solar_wind_classification/blob/master/web/images_readme/log.PNG)


## Authors:

* **Jing Li** - jingli18@bu.edu - *Model Design*
* **Mingdao Che** - mdche@bu.edu - *Website*

## Citing literature:
[Classification of Solar Wind With Machine Learning Enrico Camporeale  Algo Carè  Joseph E. Borovsky First published: 16 October 2017](https://agupubs.onlinelibrary.wiley.com/doi/abs/10.1002/2017JA024383)
