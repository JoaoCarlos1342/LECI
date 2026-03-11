//
// Algoritmos e Estruturas de Dados --- 2024/2025
//
// J. Madeira - Dec 2023, Dec 2024
//

#include <iostream>
#include <map>

using namespace std;

int main(void) {
  map<string, unsigned> m;

  // display map size
  cout << " " << m.size() << endl;

  // insert some (key,value) pairs
  m["February"] = 2;
  m["April"] = 4;
  m.insert({"May", 5});
  m.insert({"January", 1});
  m.insert({"March", 3});
  m["December"] = 12;

  // use key to get value
  cout << "key = January value = " << m.at("January") << endl;
  cout << "key = February value = " << m["February"] << endl;

  cout << endl;

  // list contents using iterator loop
  for (const auto& e : m) {
    cout << "key = " << e.first << " value = " << e.second << endl;
  }

  cout << endl;

  // list contents with an explicit iterator
  for (auto it = m.begin(); it != m.end(); ++it) {
    cout << "key = " << (*it).first << " value = " << (*it).second << endl;
  }

  return (0);
}