//
// Algoritmos e Estruturas de Dados --- 2024/2025
//
// J. Madeira - Dec 2023, Dec 2024
//

#include <iostream>
#include <queue>

using namespace std;

int main(void) {
  queue<size_t> uint_queue;

  // display size of empty queue
  cout << " " << uint_queue.size() << endl;

  // push into the back of the queue
  for (size_t i = 0; i < 10; ++i) {
    uint_queue.push(i);
  }

  // peek and pop from the front of the queue
  while (!uint_queue.empty()) {
    std::cout << uint_queue.front() << std::endl;
    uint_queue.pop();
  }

  return (0);
}