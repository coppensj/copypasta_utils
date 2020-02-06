//make sure to add '-lstdc++fs' to LDFLAGS in the makefile

#include <experimental/filesystem>
#include <iostream>

namespace fs = std::experimental::filesystem;

int main(){

    fs::path folderpath = fs::current_path() / "test_folder";

    if(fs::remove(folderpath))
        std::cout << folderpath << " was successfully deleted.\n";
    else
        std::cout << folderpath << " does not exist.\n";

    return 0;
}
