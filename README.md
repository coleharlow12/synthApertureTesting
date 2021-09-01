# synthApertureTesting

#Overview
The purpose of this script is to allow control of a Prusa MK2 Printer along with a TI IWR6843 ISK-ODS Radar. The script allows users to use a 3D printer to scan a TI board to create a synthetic aperture array radar

# FullControl.py
The primary algorithm to run is the fullControl.py script. This function controls both the printer and radar module to create a Synthetic aperture radar. Other libraries and functions within this project are called by fullControl.py. Prior to running the full Control algorithm the user must make all the connections specified below as well as configure the radar using mmWave Studio (see TI Radar Module Control). Within fullControl the user can configure the stops of the radar using the PreMeas function. Currently the algorithm only supports rectangular apertures. Following completion of the script radar data for each stop is stored separately. For this reason the function outputs three files/folders. 1st a new measurement<num>  folder within the Measurement folder. 2nd an excel sheet which contains the stop number and location of each stop. Third radar is stored in binary files with the stop number labelled. Binary files are read using the readDCA1000.m file found in the synthApertureImaging library.

# Prusa Control
Prusa Control is done through the use of a USB-B cord connected to directly from the computer to the USB-B Female port of the Prusa MK2. For this reason prior to running the script the correct port of the USB-B will have to be identified in the computer and input into the "ser" variable of fullControl.py. The baudrate of the printer connection will need to be 115200 which is specified along with the port number. Control of the prusa is down through python and requires the following libraries.

### Dependencies
- python serial library
- os library
- time library

# TI Radar Module Control
The TI radar module is controlled through mmWaveStudio. To connect the radar follow guidelines in the mmWaveStudio user manual as well as the user manual for the specific chip being used. Prior to running the fullControl.py algorithm to take measurements it is necessary for the user to fully connect and configure the TI mmWave radar through mmWaveStudio. Typically it is good to manually take a test through mmWave Studio to ensure proper functioning. Once TI mmWave studio is configured the fullControl.py algorithm can be run. This python script calls matlab through python. The matlab script then executes a command which communicates with TI mmWaveStudio to take measurements and store them in a file. At the start of the fullControl.py algorithm a new folder will be created in the Measurement folder with name Measurement<num> where num is the first available measurement number. 

### Dependencies
- matlab engine
- python 2.7, 3.7 or 3.8 which are only supported versions for matlab engine.





