cmake_minimum_required(VERSION 3.13)
project(LibboardTest CXX)

find_package(Libboard REQUIRED)

add_executable(example example.cpp)
target_link_libraries(example Libboard::Libboard)
