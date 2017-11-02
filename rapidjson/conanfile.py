from conans import ConanFile

class RapidjsonConan(ConanFile):
    name = "RapidJSON"
    version = "1.1.0"
    license = "https://github.com/miloyip/rapidjson/blob/master/license.txt"
    url = "https://github.com/dorant/conan-recipes"
    description = "A fast JSON parser/generator for C++ with both SAX/DOM style API"

    def source(self):
        self.run("git clone --depth=1 https://github.com/miloyip/rapidjson -b v%s" % self.version)

    def package(self):
        self.copy('*', dst='include', src='rapidjson/include')
