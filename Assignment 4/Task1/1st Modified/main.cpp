#include <iostream>
#include <boost/tokenizer.hpp>

// Q#4 Twice my_header_file.hpp 
#include "my_header_file.hpp"
#include "my_header_file.hpp"
int main() {
MyClass obj;
std::cout << "MyClass Object is Added" << std::endl;
std::cout << "File Inclusions Test" << std::endl;
return 0;
}