// Last updated: 19/10/2026, 16:20:15
class Solution {
public:
    int helper(vector<int>& nums) {
        int i = 0;
        int msum = INT_MAX;
        for (int j = 0; j < nums.size() - 1; j++) {
            int sum = nums[j] + nums[j + 1];
            if (sum < msum) {
                i = j;
                msum = min(msum, sum);
            }
        }

        return i;
    }
    bool isSorted(vector<int>& nums) {
        bool flag = true;
        for (int i = 0; i < nums.size() - 1; i++) {
            if (nums[i + 1] < nums[i]) {
                flag = false;
            }
        }
        return flag;
    }
    int minimumPairRemoval(vector<int>& nums) {
        int step = 0;
        while (!isSorted(nums)) {
            int i = helper(nums);
            nums[i] += nums[i+1];
            nums.erase(nums.begin() + i + 1);
            step++;
        }

        return step;
    }
};