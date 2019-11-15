cmake_minimum_required(VERSION 2.6)

project(test)

# The version number
set(Test_VERSION_MAJOR 1)
set(Test_VERSION_MINOR 0)

# config
configure_file(
    "${PROJECT_SOURCE_DIR}/TestConfig.h.in"
    "${PROJECT_BINARY_DIR}/TestConfig.h"
)

include_directories("${PROJECT_BINARY_DIR}")

add_executable(main main.cpp)

