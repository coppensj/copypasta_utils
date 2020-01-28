//make sure to add '-lstdc++fs' to LDFLAGS in the makefile

#include <experimental/filesystem>
#include <string>
#include <iostream>

namespace fs = std::experimental::filesystem;

int main(){

    std::string foldername = "test_folder";

    fs::create_directory(foldername);

    return 0;
}
