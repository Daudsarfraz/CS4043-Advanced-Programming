#include <iostream>
#include <boost/tokenizer.hpp>

// Q#4 Twice my_header_file.hpp 
#include "my_header_file.hpp"
//#include "my_header_file.hpp"
int main() {
MyClass obj;
std::cout << "#ifdef is Added" << std::endl;
std::cout << "MyClass Object is Added" << std::endl;
std::cout << "Twice same.hpp is Added" << std::endl;
std::cout << "File Inclusions Test" << std::endl;
return 0;
}