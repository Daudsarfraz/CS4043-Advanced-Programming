#ifndef MY_HEADER_FILE_HPP
#define MY_HEADER_FILE_HPP
#include <iostream>
// Q#1. Create a macro in the header file:
#define isodd(param1) (param1 % 2 !=0)
class MyClass {
public:
    void myFunction(int x) {
        // Q#2 if else conditions -> #if and #endif blocks
        #if isodd(x) == 0
            std::cout << "even" << std::endl;
        #else
            std::cout << "odd" << std::endl;
        #endif
    }
};
#endif
