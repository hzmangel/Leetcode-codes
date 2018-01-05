#include <vector>
#include <iostream>
using namespace std;

class Solution {
public:
    int rob(vector<int>& nums) {
        int sz = nums.size();
        if (sz == 0) {
            // No house available
            return 0;
        } else if (sz == 1) {
            return nums[0];
        } else if (sz == 2) {
            return max(nums[0], nums[1]);
        } else if (sz == 3) {
            return max(nums[0]+nums[2], nums[1]);
        }

        // For more than three houses, the max money started from house i is
        // S[i] = nums[i] + max(S[i+2], S[i+3])
        vector<int> partial_result;
        partial_result.resize(sz);
        partial_result[sz-1] = nums[sz-1];
        partial_result[sz-2] = max(nums[sz-1], nums[sz-2]);
        partial_result[sz-3] = max(nums[sz-1]+nums[sz-3], nums[sz-2]);

        for (int i  = sz - 4; i >= 0; i--) {
            partial_result[i] = nums[i] + max(partial_result[i+2], partial_result[i+3]);
        }

        return max(max(partial_result[0], partial_result[1]), partial_result[2]);
    }

private:
    int max(int i, int j) {
        if (i > j) {
            return i;
        } else {
            return j;
        }
    }
};

int main() {
    Solution *foo = new Solution();
    vector<int> houses{1,2,3,4,5,6,7,8,9};
    cout << "Result is: " << foo->rob(houses) << endl;
}

