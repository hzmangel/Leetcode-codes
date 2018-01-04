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

class NumArray {
    private:
        vector<int> partial_sums;
    public:
        NumArray(vector<int> nums) {
            int tmp_sum = 0;
            partial_sums.push_back(tmp_sum);  // For first element
            for (auto &n: nums) {
                tmp_sum += n;
                partial_sums.push_back(tmp_sum);
            }
            print_vector(partial_sums);
        }

        int sumRange(int i, int j) {
            int partial_sum_size = partial_sums.size();
            // i and j are all inclusived, so use size-2 as upper boundary
            if (j > partial_sum_size-1) {
                j = partial_sum_size-1;
            }

            if (i < 0) {
                i = 0;
            }

            return partial_sums[j+1] - partial_sums[i];
        }
};

int main() {
    vector<int> nums{-2,0,3,-5,2,-1};
    NumArray *obj = new NumArray(nums);
    cout << obj->sumRange(0, 2) << endl;
    cout << obj->sumRange(2, 5) << endl;
    cout << obj->sumRange(0, 5) << endl;
}

