//make sure to add '-lstdc++fs' to LDFLAGS in the makefile

#include <experimental/filesystem>

namespace fs = std::experimental::filesystem;

int main(){
    
    fs::path foldername = "test_folder";

    fs::create_directory(fs::current_path() / foldername);

    return 0;
}
