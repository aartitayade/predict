==================
BikeShareData_Reg
==================

This projest predicts the rental bike sharing counts on the basis of different environmental and weather situations such as
temperature, humidity and windspeed etc.

=========
Overview
=========

Bike-sharing rental process is highly correlated to the environmental and seasonal settings. For instance, weather conditions,
precipitation, day of week, season, hour of the day, etc. can affect the rental behaviors. The core data set is related to  
the two-year historical log corresponding to years 2011 and 2012 from Capital Bikeshare system, Washington D.C., USA which is 
publicly available in http://capitalbikeshare.com/system-data.

The dataset is taken from the publicly available in http://archive.ics.uci.edu/ml/datasets/bike+sharing+dataset

=============
Prerequisite
=============

make sure you have following prerequisites

python_requires= python >=3.6

following is the list of libraries ,need to install for this project.
1. pandas
2. sklearn
3. matplotlib
4. numpy

test_requires= pytest

STRAT --> cmd / shell

$pip install pandas
$pip install -U scikit-learn
$pip install matplotlib
$pip install numpy

$pip install pytest

Donwload data from http://archive.ics.uci.edu/ml/datasets/bike+sharing+dataset

save day.csv under /src/ folder

======
To Do
======
1. Import the libraries: first import all the libraries and module that we are going to use in this project.
2. Load the data: load the dataset using pandas from csv

3. Summarize the data: here also we use pandas to explore the data with descriptive statistics and visualization.

4. Build model: we are using sklerarns LinearRegression technique for preparing the model. for training the model we need to split 
   our data into training set accompanied by the label.we can build different models and estimate its accuracy score. 
   we have created three models for predicting the rental bike sharing count for different temperature, humidity and windspeed.

5. Make Predictions: once the model is fit on training data, we can make prediction on dataset. 

=============
Steps To Run 
=============
To run the python script follow the steps below.
 
1. download this repository
2. open command prompt or powershell on windows
3. go to downloaded repository/directory 
4. run command:
   pip install .
5  above command will install "predict" package
6  now run belove commands to predict total count of rented bikes 
   $predict
7 predict will ask to enter atemp,hum(humadity),windspeed values for which you want total count of bikes

 
----------------------------------------------------------------------------------------------
$ Start --> CMD
$cd predict
$ pip install .
$ predict


----------------------------------------------------------------------------------------------
