#include <iostream>
#include <cstring>

void vulnerable_function(char* input) {
    char buffer[16];
    
    // VULNÉRABILITÉ : strcpy ne vérifie pas la longueur de la chaîne source.
    // Si 'input' fait plus de 15 caractères, il y aura un dépassement de tampon.
    strcpy(buffer, input);
    
    std::cout << "Buffer content: " << buffer << std::endl;
}

int main(int argc, char** argv) {
    if (argc > 1) {
        vulnerable_function(argv[1]);
    } else {
        std::cout << "Please provide an argument." << std::endl;
    }
    return 0;
}
