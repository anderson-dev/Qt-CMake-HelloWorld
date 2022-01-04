from conans import ConanFile, MSBuild, tools

class HelloWorld(ConanFile):
     name = "HelloWorld"
     license = "BSD"
     author = "your name"
     url = "git@gitlab.com:<url/project>"
     description = "Base Library A of the example project."
     topics = ("<Put some tag here>", "<here>", "<and here>")
     settings = "os", "arch", "compiler", "build_type"
     generators = "cmake_find_package"

     def build_requirements(self):
         self.build_requires("gtest/1.8.1")

     def requirements(self):
         self.requires("qt/5.15.2")

        # def package_info(self):
        #     self.cpp_info.libs = ["BaseLibBLibrary"]