#include <fstream>

int main(){

    const char* file1_name = "file1.csv";
    const char* file2_name = "file2.csv";
    std::ofstream f1, f2;
    int LEN = 10;
    float data[LEN] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};

    f1.open(file1_name);
    for(int i=0; i<LEN; i++){
        if(i == LEN - 1) f1 << data[i];
        else             f1 << data[i] << ',';
    }
    f1 << std::endl;
    f1.close();
    
    f2.open(file2_name);
    for(int i=0; i<10; i++)
        f2 << i << ',' << data[i] << std::endl;
    f2.close();

    return 0;
}
