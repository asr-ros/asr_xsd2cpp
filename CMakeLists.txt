cmake_minimum_required(VERSION 2.4.6)
project(asr_xsd2cpp)

find_package(catkin)

catkin_package()

install(FILES ${PROJECT_SOURCE_DIR}/catkin_make.cmake
        DESTINATION ${CATKIN_GLOBAL_SHARE_DESTINATION}/asr_xsd2cpp)
