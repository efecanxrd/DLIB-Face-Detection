# Face Detection with DLIB
![EfecanLogo](https://avatars.githubusercontent.com/u/66366306?s=100&u=dc5e6f5b4a05d07958d9a867b803760aa2b1613e&v=4)
### In this project, we have detected our face with dlib and opencv libraries.
![XhW](https://i.imgur.com/qHAcfhX.gif)
## Setup This Project
### Install DLIB & OpenCV
- You can install the dlib library by typing ```conda install -c conda-forge dlib``` in your terminal. Anaconda must be installed.
- The easiest way to install opencv is to download it from PyPI. It's going to install the library itself and its prerequisites as well. You can install the opencv library by typing ```pip install opencv-python``` in your terminal.
- And then you can run the project with main.py. Make sure you have **"shape_predictor_68_face_landmarks.dat"** file in your project location.
- [Download shape_predictor_68_face_landmarks.dat](https://github.com/coneypo/Dlib_face_detection_from_camera/raw/master/data/dlib/shape_predictor_68_face_landmarks.dat) I could not add it to this project because it is larger than 25mb
## How this is working?
The project takes the image from the real time camera with the opencv library. We can process this data with dlib and scan 68 points on our face.

Normal            |  0          | -50                        |  -200
:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:
![](https://i.imgur.com/uAvW69p.png)  |  ![](https://i.imgur.com/0bUVmgt.png)  |  ![](https://i.imgur.com/GAK10bV.png)  |  ![](https://i.imgur.com/rXmOPGz.png)
