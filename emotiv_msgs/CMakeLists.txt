cmake_minimum_required(VERSION 2.8.3)
project(emotiv_msgs)

find_package(catkin REQUIRED std_msgs message_generation)

add_message_files(
  FILES
  Data.msg
  channels.msg
  channelData.msg
)

generate_messages(
  DEPENDENCIES
  std_msgs
)

catkin_package(
  CATKIN_DEPENDS message_runtime
)
