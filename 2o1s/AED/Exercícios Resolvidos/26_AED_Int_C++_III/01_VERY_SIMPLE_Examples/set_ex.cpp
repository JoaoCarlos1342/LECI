//
// Algoritmos e Estruturas de Dados --- 2024/2025
//
// J. Madeira - Dec 2023, Dec 2024
//

#include <iostream>
#include <set>

using namespace std;

int main(void) {
  set<string> s;

  // display set size
  cout << " " << s.size() << endl;

  // add elements to the set
  // what happens if we attempt to add an element
  // that already exists in the set?
  s.insert("February");
  s.insert("April");
  s.insert("May");
  s.insert("January");
  s.insert("March");
  s.insert("December");
  s.insert("March");
  s.erase("March");

  cout << endl;

  // Display all set elements
  for (const auto& e : s) {
    cout << e << endl;
  }

  cout << endl;

  // Display all set elements
  // explicitly using an iterator
  for (auto it = s.begin(); it != s.end(); ++it) {
    cout << (*it) << endl;
  }

  cout << endl;

  // Display all set elements in REVERSE order
  auto it = --s.end();  // referencing the last element
  for (; it != s.begin(); --it) {
    cout << (*it) << endl;
  }
  cout << (*it) << endl;

  return (0);
}