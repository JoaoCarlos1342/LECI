//
// Algoritmos e Estruturas de Dados --- 2024/2025
//
// J. Madeira - Dec 2023, Dec 2024
//

#include <iostream>
#include <stack>

using namespace std;

int main(void) {
  stack<size_t> uint_stack;

  // display stack size
  cout << " " << uint_stack.size() << endl;

  // Pushing
  for (size_t i = 0; i < 10; ++i) {
    uint_stack.push(i);
  }

  // Peeking and poping
  while (!uint_stack.empty()) {
    std::cout << uint_stack.top() << std::endl;
    uint_stack.pop();
  }

  return (0);
}