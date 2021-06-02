# Remote Monitoring of Heart Rate
A mobile app based on Kivy Framework and Python.
The input of the app is a video of user's face approximately to 5-8 seconds.
The output is the user's heart rate.

# Method:
In this method there are 5 stages:
-Face Recognition
-Preprocessing image(Laplacian Pyramid)
-Eulerian magnification and Band pass filtering
-Heart rate calculation
-Kivy app for android

## Program organization:
The main.py file contains the main program that utilizes all of the other modules defined in the other code files
to read in the input video, run Eulerian magnification on it, and to display the results. The purposes of the other
files are described below:
- face_recognition.py - Contains function to read in video from file and uses Haar cascade face detection to detect the face.
- laplacian_pyramid.py - Contains functions to apply spatial filtering on video using the method of laplacian-gaussian pyramid.
- eulerian.py - Contains function for a temporal bandpass filter that uses a Fast-Fourier Transform
- heartrate_calculation.py - Contains function to calculate heart rate from FFT results
- heart_rate_calculator_application.py - Contains function calling all the aforementioned.
- kivy_manager.kv - Contains rules and root widgets for the app.
- main.py - Contains classes and functions connecting the mobile app with the heart_rate_calculator_application.py

## How to convert Kivy to Android APK
Redirect here: ( https://github.com/attreyabhatt/Kivy-Pong-Game/blob/master/PingPong/KivyToAndroid.txt )


## How to run:
To run the app on your pc you just need to install the libraries given on requirements.txt 
The following command will install the packages according to the configuration file requirements.txt.

$ pip install -r requirements.txt

After that you can run main.py.
In order to run the app on your phone you need to follow the above instructions( How to convert Kivy to androik APK).

### This application was created for the purposes of a Biomedical Course at National Technical University of Athens.
