from conans import ConanFile, tools
import os


class JWTCppConan(ConanFile):
    name = "jwt-cpp"
    version = "0.3.1+0"
    license = "MIT License"
    url = "https://github.com/odant/conan-jwtcpp"
    description = "JWTCpp library"
    exports_sources = "src/*"
    no_copy_source = True

    def requirements(self):
        self.requires("openssl/1.1.0k@odant/stable")

    def package(self):
        self.copy(pattern="*", src="src/include", dst="include")

    def package_id(self):
        self.info.header_only()
