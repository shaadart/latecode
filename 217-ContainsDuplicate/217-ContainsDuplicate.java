// Last updated: 4/16/2026, 6:17:26 AM
1class Solution {
2    public boolean containsDuplicate(int[] nums) {
3        HashSet<Integer> seenNumbers = new HashSet<>();
4
5        for (int num : nums){
6            if (seenNumbers.contains(num)){
7                return true;
8            }
9            seenNumbers.add(num);
10        }
11        return false;
12    }
13}