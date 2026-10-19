// Last updated: 19/10/2026, 16:29:33
class Solution {
  int majorityElement(List<int> nums) {
    nums.sort();
    return nums[nums.length ~/ 2];
  }
}