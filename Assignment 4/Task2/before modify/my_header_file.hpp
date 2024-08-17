#ifndef MY_HEADER_FILE_HPP
#define MY_HEADER_FILE_HPP

#include <iostream>

class MyClass {
public:
    void myFunction(int x) {
        // Q#2
        #if isodd(x) == 0
            std::cout << "even" << std::endl;
        #else
            std::cout << "odd" << std::endl;
        #endif
    }
};

#endif
