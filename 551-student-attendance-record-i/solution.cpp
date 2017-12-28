#include <string>
#include <iostream>
using namespace std;

class Solution {
public:
    bool checkRecord(string s) {
        int a_count = 0;
        int l_count = 0;

        for (auto &c: s) {
            switch(c) {
                case 'A':
                    // This is not L, set l_count back to 0
                    l_count = 0;
                    if (a_count > 0) {
                        // Already got an A before, failed
                        return false;
                    }
                    a_count++;
                    break;
                case 'L':
                    if (l_count == 2) {
                        // Already have 2 L, failed
                        return false;
                    } else {
                        l_count++;
                    }
                    break;
                case 'P':
                    l_count = 0;
                    break;
            }
        }

        return true;
    }

};

int main() {
    auto foo = new Solution();
    cout << foo->checkRecord("PPALLP") << endl;
    cout << foo->checkRecord("PPALLL") << endl;
    cout << foo->checkRecord("PPAPAL") << endl;
}
