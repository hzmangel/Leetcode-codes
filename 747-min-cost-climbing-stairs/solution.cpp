#include <vector>
#include <iostream>
using namespace std;

template <typename T>
void print_vector(vector<T> vec) {
    cout << "Vec size: " << vec.size() << endl;
    for (auto &el: vec) {
        cout << el << ", ";
    }
    cout << endl;
}

class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
       int cost_size = cost.size();
       if (cost_size == 0) {
           return 0;
       }

       // For case that doesn't match the formula
       if (cost_size == 1) {
           return cost[0];
       } else if (cost_size == 2) {
           return min(cost[0], cost[1]);
       }

       // Variable saves cost
       vector<int> middle_steps(cost_size);

       // Init state, for last 2 steps
       middle_steps[cost_size-1] = cost[cost_size-1];
       middle_steps[cost_size-2] = cost[cost_size-2];

       for (int i = cost_size-3; i >= 0; i--) {
           middle_steps[i] = cost[i] + this->min(middle_steps[i+1], middle_steps[i+2]);
       }
       print_vector(middle_steps);

       return min(middle_steps[0], middle_steps[1]);
    }

private:
    int min(int a, int b) {
        if (a > b) {
            return b;
        } else {
            return a;
        }
    }
};

int main() {
    Solution *foo = new Solution();
    //vector<int> steps{10, 15, 20};
    vector<int> steps{1, 100, 1, 1, 1, 100, 1, 1, 100, 1};
    int rslt = foo->minCostClimbingStairs(steps);
    cout << "Result is: " << rslt << endl;
}
