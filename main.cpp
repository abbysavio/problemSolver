#include <iostream>
#include <fstream>
#include <sstream>
#include <cstdlib>

std::string readFile(const std::string& path) {
    std::ifstream file(path);
    std::stringstream buffer;
    buffer << file.rdbuf();
    return buffer.str();
}

void sendToGemini(const std::string& code) {
    std::ofstream out("input.txt");
    out << code;
    out.close();

    std::cout << "Sending to Gemini...\n";
    std::system("python3 send_to_gemini.py input.txt");
}

int main() {
    std::string path;
    std::cout << "Enter path to your LeetCode solution (.cpp): ";
    std::getline(std::cin, path);

    std::string code = readFile(path);
    sendToGemini(code);

    return 0;
}
