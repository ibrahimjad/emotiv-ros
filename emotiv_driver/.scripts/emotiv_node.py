#!/usr/bin/env python

import rospy
import sys
from emotiv_msgs.msg import Data
from emokit.emotiv import Emotiv
from emokit.packet import EmotivExtraPacket

sys.tracebacklimit=0

channels = ['AF3', 'F7', 'F3', 'FC5', 'T7', 'P7', 'O1', 'O2', 'P8', 'T8', 'FC6', 'F4', 'F8', 'AF4']

def updateMsg(packet, msg):
    msg.header.stamp = rospy.Time.now()

    msg.channel.O1.data = packet.sensors['O1']['value']
    msg.channel.O2.data = packet.sensors['O2']['value']

    msg.channel.O1.quality = packet.sensors['O1']['quality']
    msg.channel.O2.quality = packet.sensors['O2']['quality']

if __name__ == '__main__':
    pub = rospy.Publisher('emotiv_raw', Data, queue_size=1000)
    rospy.init_node('emotiv_node')
    rospy.loginfo("Trying to connect to headset")
    isFirstRun = True
    rate = rospy.Rate(256)
    msg = Data()

    with Emotiv(display_output=False, verbose=False, write=False, force_epoc_mode=True, is_research=True) as headset:
        while not rospy.is_shutdown():
            try:
                packet = headset.dequeue()
                if packet is not None:
                    if isFirstRun:
                        rospy.loginfo("Connected to headset successfully")
                        isFirstRun = False
                    if type(packet) != EmotivExtraPacket:
                        updateMsg(packet, msg)
                        pub.publish(msg)
                rate.sleep()
            except rospy.ROSInterruptException:
                headset.stop()
