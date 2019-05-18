#!/usr/bin/env python

import rospy
import sys
from emotiv_msgs.msg import Data
from emokit.emotiv import Emotiv
from emokit.packet import EmotivExtraPacket

sys.tracebacklimit=0

def updateMsg(packet, msg):
    msg.header.stamp = rospy.Time.now()

    msg.channel.AF3.data = packet.sensors['AF3']['value']
    msg.channel.F7.data = packet.sensors['F7']['value']
    msg.channel.F3.data = packet.sensors['F3']['value']
    msg.channel.FC5.data = packet.sensors['FC5']['value']
    msg.channel.T7.data = packet.sensors['T7']['value']
    msg.channel.P7.data = packet.sensors['P7']['value']
    msg.channel.O1.data = packet.sensors['O1']['value']
    msg.channel.O2.data = packet.sensors['O2']['value']
    msg.channel.P8.data = packet.sensors['P8']['value']
    msg.channel.T8.data = packet.sensors['T8']['value']
    msg.channel.FC6.data = packet.sensors['FC6']['value']
    msg.channel.F4.data = packet.sensors['F4']['value']
    msg.channel.F8.data = packet.sensors['F8']['value']
    msg.channel.AF4.data = packet.sensors['AF4']['value']

    msg.channel.AF3.quality = packet.sensors['AF3']['quality']
    msg.channel.F7.quality = packet.sensors['F7']['quality']
    msg.channel.F3.quality = packet.sensors['F3']['quality']
    msg.channel.FC5.quality = packet.sensors['FC5']['quality']
    msg.channel.T7.quality = packet.sensors['T7']['quality']
    msg.channel.P7.quality = packet.sensors['P7']['quality']
    msg.channel.O1.quality = packet.sensors['O1']['quality']
    msg.channel.O2.quality = packet.sensors['O2']['quality']
    msg.channel.P8.quality = packet.sensors['P8']['quality']
    msg.channel.T8.quality = packet.sensors['T8']['quality']
    msg.channel.FC6.quality = packet.sensors['FC6']['quality']
    msg.channel.F4.quality = packet.sensors['F4']['quality']
    msg.channel.F8.quality = packet.sensors['F8']['quality']
    msg.channel.AF4.quality = packet.sensors['AF4']['quality']


def main():
    pub = rospy.Publisher('emotiv_raw', Data, queue_size=1000)
    rospy.init_node('emotiv_node')
    rate = rospy.Rate(256)
    msg = Data()

    with Emotiv(display_output=False, verbose=False, write=False, force_epoc_mode=True, is_research=True) as headset:
        while not rospy.is_shutdown():
            try:
                packet = headset.dequeue()
                if packet is not None:
                    if type(packet) != EmotivExtraPacket:
                        updateMsg(packet, msg)
                        pub.publish(msg)
                rate.sleep()
            except rospy.ROSInterruptException:
                headset.stop()


if __name__ == '__main__':
    main()
