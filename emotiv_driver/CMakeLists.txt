cmake_minimum_required(VERSION 2.8.3)
project(emotiv_driver)

find_package(catkin)

catkin_package(
)

install(FILES
  launch/headset.launch
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)
