# Test for HowardHinnant/date Conan package
# Dmitriy Vetutnev, ODANT, 2018


project(PackageTest CXX)
cmake_minimum_required(VERSION 3.0)


include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)


enable_testing()

find_package(GTest REQUIRED)
find_package(GMock REQUIRED)

# Conan imported targets

add_executable(test_jwtcpp_CONAN_PKG
    TestMain.cpp
    BaseTest.cpp
    ClaimTest.cpp
    HelperTest.cpp
    TokenFormatTest.cpp
    TokenTest.cpp)
target_link_libraries(test_jwtcpp_CONAN_PKG CONAN_PKG::jwt-cpp GTest::Main GMock::GMock)
set_target_properties(test_jwtcpp_CONAN_PKG
    PROPERTIES
    INSTALL_RPATH "$ORIGIN"
    BUILD_WITH_INSTALL_RPATH True
)
add_test(
    NAME test_jwtcpp_CONAN_PKG
    WORKING_DIRECTORY ${CMAKE_BINARY_DIR}/bin
    COMMAND test_jwtcpp_CONAN_PKG
)

