cmake_minimum_required(VERSION 3.0.2)
project(service_node)

find_package(catkin REQUIRED COMPONENTS message_generation std_msgs)

add_message_files(DIRECTORY msg FILES Floats.msg HeaderString.msg)
add_service_files(DIRECTORY srv FILES AddTwoInts.srv BadTwoInts.srv)

generate_messages(DEPENDENCIES std_msgs)

catkin_package(CATKIN_DEPENDS message_runtime std_msgs)

# do not wildcard install files since the root folder of the package will contain a debian folder for releasing

catkin_install_python(PROGRAMS
  scripts/add_two_ints_client
  scripts/add_two_ints_server
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/scripts
)

c

if(CATKIN_ENABLE_TESTING)
  find_package(rostest)
  foreach(T
      test/test-add-two-ints.launch

      test/test-on-shutdown.launch
      test/test-connection-header.launch)
     add_rostest(${T})
  endforeach()
endif()
