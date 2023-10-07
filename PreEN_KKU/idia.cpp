#include <iostream>

int main() {
    int x;
    std::cin >> x;

    if (x == 1) {
        std::cout << "ON" << std::endl;
    } else if (x == 0) {
        std::cout << "OFF" << std::endl;
    } else {
        std::cout << "ERROR" << std::endl;
    }

    return 0;
}


