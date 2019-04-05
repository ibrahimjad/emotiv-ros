# Emotiv ROS package

**ROS package for getting raw EEG signals from Emotiv Epoc+ Headset**

This package is based on [Emokit](https://github.com/openyou/emokit) by The OpenYou Organization.

## Installation
Change directory to your ROS workspace and then type the following:

`cd src`

`git clone https://github.com/ibrahimjad/emotiv-ros.git`

`cd ..`

`catkin build emotiv_driver emotiv_msgs`

`source ~/.bashrc`

## Usage
A pre-compiled binary can be used to start up quickly using the following command:

`rosrun emotiv_driver emotiv_node`

This will publish raw EEG signals of channel *O1* and *O2* to **/emotiv_raw** topic

Raw data should be around 4k and contact quality above 3k for getting good readings
