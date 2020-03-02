# Emotiv ROS package

**ROS package for getting raw EEG signals from Emotiv EPOC+ Headset**

This package is based on [Emokit](https://github.com/openyou/emokit) by The OpenYou Organization.

## Prerequisits

* hidapi - https://github.com/signal11/hidapi

## Installation
Change directory to your ROS workspace and then type the following:

```bash
cd src
git clone https://github.com/ibrahimjad/emotiv-ros.git
sudo mv -f emotiv-ros/emotiv_driver/epoc.rules /etc/udev/rules.d/
cd ../

catkin build emotiv_driver emotiv_msgs
source ~/.bashrc
```

## Usage
A pre-compiled binary can be used to start up quickly using the following command:
```bash
roslaunch emotiv_driver headset.launch
```

This will publish raw EEG signals of all channels to **/emotiv_raw** topic

Raw data should be around 4k and contact quality above above 1k for getting good readings

Otherwise if you do not wish to use the pre-compiled binary, the python script in [emotiv_driver/.scripts/emotiv_node.py](emotiv_driver/.scripts/emotiv_node.py) can be used but requires installing the additional dependencies as shown in [Emokit](https://github.com/openyou/emokit).