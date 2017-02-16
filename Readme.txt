How to use xmlschemagen?

Step 0: Add the package to your ros workspace.
Step 1: Create a XMLSchema according to the W3C specification and store them in a folder named "xsd" with extension ".xsd"
Step 2: Add the following lines to your CMakeLists.txt

# Create C++ files from xsd
rosbuild_find_ros_package(xmlschemagen REQUIRED)
include(${xmlschemagen_PACKAGE_PATH}/rosbuild.cmake)
xmlschemagen()

Step 3: call 'make' and the files will be generated automatically.
Step 4: There is no Step 4!

Bugreports to mail@ralfschleicher.de