# jetsonNano_glasses
Project for Jetson AI specialist certification


# Description
This poject attempts to solve a difficult problem: how to find your glasses if you've lost them, because you can't see them! 
Transfer learning was used to train SSD-Mobilenet-V2 for object detection on a custom dataset of glasses lying about various places. 
A custom python program was then written following the instructions in the Hello AI World tutorial, linked below, to run the model and locate lost glasses. 

# What all is in this repository?
The file detection.py is the main python file which, when run, will provide real-time detection and location of glasses.
The Model directory contains the retrained neural network for object detection. 
The Data directory stores the dataset that the model was trained on. 

# Instructions!
- Install JetPack 4.5 and Jetson-Inference by following these instructions: https://github.com/dusty-nv/jetson-inference/blob/master/docs/jetpack-setup-2.md
- Clone this repository into your home directory by running this command:
``` bash 
$ git clone https://github.com/LParker885/GlassesDetectnet.git
```
Move to the model directory and extract the model file:
``` bash
$ cd GlassesDetectnet/Model
$ tar -xvf ssd-mobilenet.onnx.tar.gz
```
- Plug in a compatable USB camera: the Logitech C270 camera is reccomended because that is what the project was tested with, but other compatible cameras should work. 
- Navigate to the GlassesDetectnet directory and run the python script to find your glasses! (It may take a few seconds to start up, but once running it should get about 40 FPS in MAXN power mode.)
- For best results, use glasses with thick black frames such as the ones that can be seen in the photos in the Data directory.  
``` bash
$ cd ~/GlassesDetectnet
$ python3 detection.py
``` 
