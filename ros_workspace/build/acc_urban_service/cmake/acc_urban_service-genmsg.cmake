# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "acc_urban_service: 0 messages, 1 services")

set(MSG_I_FLAGS "-Istd_msgs:/opt/ros/noetic/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(acc_urban_service_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/ubuntu20/ros_workspace/src/acc_urban_service/srv/YoloData.srv" NAME_WE)
add_custom_target(_acc_urban_service_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "acc_urban_service" "/home/ubuntu20/ros_workspace/src/acc_urban_service/srv/YoloData.srv" ""
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages

### Generating Services
_generate_srv_cpp(acc_urban_service
  "/home/ubuntu20/ros_workspace/src/acc_urban_service/srv/YoloData.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/acc_urban_service
)

### Generating Module File
_generate_module_cpp(acc_urban_service
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/acc_urban_service
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(acc_urban_service_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(acc_urban_service_generate_messages acc_urban_service_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/ubuntu20/ros_workspace/src/acc_urban_service/srv/YoloData.srv" NAME_WE)
add_dependencies(acc_urban_service_generate_messages_cpp _acc_urban_service_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(acc_urban_service_gencpp)
add_dependencies(acc_urban_service_gencpp acc_urban_service_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS acc_urban_service_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages

### Generating Services
_generate_srv_eus(acc_urban_service
  "/home/ubuntu20/ros_workspace/src/acc_urban_service/srv/YoloData.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/acc_urban_service
)

### Generating Module File
_generate_module_eus(acc_urban_service
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/acc_urban_service
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(acc_urban_service_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(acc_urban_service_generate_messages acc_urban_service_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/ubuntu20/ros_workspace/src/acc_urban_service/srv/YoloData.srv" NAME_WE)
add_dependencies(acc_urban_service_generate_messages_eus _acc_urban_service_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(acc_urban_service_geneus)
add_dependencies(acc_urban_service_geneus acc_urban_service_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS acc_urban_service_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages

### Generating Services
_generate_srv_lisp(acc_urban_service
  "/home/ubuntu20/ros_workspace/src/acc_urban_service/srv/YoloData.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/acc_urban_service
)

### Generating Module File
_generate_module_lisp(acc_urban_service
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/acc_urban_service
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(acc_urban_service_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(acc_urban_service_generate_messages acc_urban_service_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/ubuntu20/ros_workspace/src/acc_urban_service/srv/YoloData.srv" NAME_WE)
add_dependencies(acc_urban_service_generate_messages_lisp _acc_urban_service_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(acc_urban_service_genlisp)
add_dependencies(acc_urban_service_genlisp acc_urban_service_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS acc_urban_service_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages

### Generating Services
_generate_srv_nodejs(acc_urban_service
  "/home/ubuntu20/ros_workspace/src/acc_urban_service/srv/YoloData.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/acc_urban_service
)

### Generating Module File
_generate_module_nodejs(acc_urban_service
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/acc_urban_service
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(acc_urban_service_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(acc_urban_service_generate_messages acc_urban_service_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/ubuntu20/ros_workspace/src/acc_urban_service/srv/YoloData.srv" NAME_WE)
add_dependencies(acc_urban_service_generate_messages_nodejs _acc_urban_service_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(acc_urban_service_gennodejs)
add_dependencies(acc_urban_service_gennodejs acc_urban_service_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS acc_urban_service_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages

### Generating Services
_generate_srv_py(acc_urban_service
  "/home/ubuntu20/ros_workspace/src/acc_urban_service/srv/YoloData.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/acc_urban_service
)

### Generating Module File
_generate_module_py(acc_urban_service
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/acc_urban_service
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(acc_urban_service_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(acc_urban_service_generate_messages acc_urban_service_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/ubuntu20/ros_workspace/src/acc_urban_service/srv/YoloData.srv" NAME_WE)
add_dependencies(acc_urban_service_generate_messages_py _acc_urban_service_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(acc_urban_service_genpy)
add_dependencies(acc_urban_service_genpy acc_urban_service_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS acc_urban_service_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/acc_urban_service)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/acc_urban_service
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(acc_urban_service_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/acc_urban_service)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/acc_urban_service
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(acc_urban_service_generate_messages_eus std_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/acc_urban_service)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/acc_urban_service
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(acc_urban_service_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/acc_urban_service)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/acc_urban_service
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(acc_urban_service_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/acc_urban_service)
  install(CODE "execute_process(COMMAND \"/usr/bin/python3\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/acc_urban_service\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/acc_urban_service
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(acc_urban_service_generate_messages_py std_msgs_generate_messages_py)
endif()
