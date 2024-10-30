To install the proper python packages to run opencv to read QR codes with the picamera3 module, we can continue to use the requirements.txt file from face expression. To do this:
Create a virtual environment that has site packages
python -m venv --system-site-packages [name of virtualenv]
Load the venv
source [name of virtualenv]/bin/activate
Then you should be able to install of the required packages:
pip install -r requirements.txt
If you forget to do any of this, the issues that occur are:
Picamera2, the module needs for using the picam in python, can’t be installed via pip and can only be installed using sudo apt install which installs it for the whole system and no for the venv
If you try to install the requirements for the whole system, using sudo apt install, there is no matching package for opencv-contrib-python which is needed for Aruco
The next step is to get everything to start on startup. 
https://learn.sparkfun.com/tutorials/how-to-run-a-raspberry-pi-program-on-startup/method-2-autostart make sure the python path is to the venv version of python


