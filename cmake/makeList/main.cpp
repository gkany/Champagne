#include <iostream>
using namespace std;

#include "TestConfig.h"

int sqrt(int n)
{
    return n*n;
}

void print_version()
{
    cout << "version: " << Test_VERSION_MAJOR << "." << Test_VERSION_MINOR << endl;
}

int main()
{
    cout << "main" << endl;
    int num = 15;
    cout << num << " sqrt is " << sqrt(num) << endl;
    
    print_version();

    return 0;
}
