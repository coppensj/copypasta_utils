#include <random>
#include <iostream>

void random_ints(int *data, int len){
    std::random_device rd;
    std::mt19937 generator (rd());
    std::uniform_int_distribution<int> rand_ints(0, 100); //random ints between 0-100
    for(int i=0; i<len; i++)
        data[i] = rand_ints(generator);
}

void random_floats(float *data, int len){
    std::random_device rd;
    std::mt19937 generator (rd());
    std::normal_distribution<float> rand_floats(0, 1); //random ints with mean 0 and stddev 1
    for(int i=0; i<len; i++)
        data[i] = rand_floats(generator);
}

int main(){

    int random_int_array[10] = {};
    random_ints(random_int_array, 10);
    std::cout << "Uniform random integers:\n";
    for(int i=0; i<10; i++)
        std::cout << i << " " << random_int_array[i] << std::endl;

    float random_float_array[10] = {};
    random_floats(random_float_array, 10);
    std::cout << "Gaussian random floats:\n";
    for(int i=0; i<10; i++)
        std::cout << i << " " << random_float_array[i] << std::endl;

    return 0;
}
