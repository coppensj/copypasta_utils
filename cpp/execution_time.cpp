#include <chrono>
#include <iostream>

int main(void){
    auto start = std::chrono::high_resolution_clock::now();

    for(unsigned long int i=0; i<1e9; i++)
        if(i % (unsigned long)1e7 == 0)
            std::cout << i << std::endl;

    auto end = std::chrono::high_resolution_clock::now();

    auto duration_ms = std::chrono::duration_cast<std::chrono::milliseconds>(end - start);
    std::cout << duration_ms.count() << " ms\n";
    std::cout << duration_ms.count()/1000.0 << " s\n";
    return 0;
}
