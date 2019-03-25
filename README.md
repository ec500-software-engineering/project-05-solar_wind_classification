# Solar_Wind_Classification_No.1
This is a final projcet for EC500 Software Engineering

## Technology:
We present a four-category classification algorithm for the solar wind, based on Gaussian Process. The four categories are: ejecta, coronal hole origin plasma, streamer belt origin plasma, and sector reversal origin plasma. The algorithm is trained and tested on a labeled portion of the OMNI data set which will be updated per day till now.The raw data is with 7 features which are **Solar wind speed(Vsw)**,
**Proton temperature standard deviation(𝜎T)**, **Sunspot number(R)**, **Solar radio flux((10.7 cm) F10.7)**, **Alfven speed(vA)**, **Proton specific entropy(Sp)**, **and Temperature ratio(Texp∕Tp)**.<br>
For these data, we plan to use Guassian process classification method.GP is a nonparametric statistical model, which has the advantage of producing probabilistic results, employing a Bayesian approach. This is a key feature that makes GP models different from most machine learning schemes. In particular, other classification schemes have the goal of finding the category boundaries in a multidimensional input space, unambiguously partitioning the input space into categories. The probabilistic approach is more flexible and informative, because it attaches a confidence level to predictions.<br>

## Environemts and APIs:
Matlab<br>

## Architecture:
![image](https://github.com/ec500-software-engineering/project-05-solar_wind_classification/blob/master/images/Blank%20Diagram.png) 

## Usage:
Just run the main.py to test the model


## Authors:

* **Jing Li** - jingli18@bu.edu - *Initial work*
* **Mingdao Che** - mdche@bu.edu - *Initial work*

## Citing literature:
[Classification of Solar Wind With Machine Learning Enrico Camporeale  Algo Carè  Joseph E. Borovsky First published: 16 October 2017](https://agupubs.onlinelibrary.wiley.com/doi/abs/10.1002/2017JA024383)
