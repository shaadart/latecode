// Last updated: 3/30/2026, 10:25:54 AM
1class Solution {
2  List<int> plusOne(List<int> digits) {
3    for (int i = digits.length - 1; i >= 0; i--) {
4      if (digits[i] == 9) {
5        digits[i] = 0;
6      } else {
7        digits[i]++;
8        return digits;
9      }
10    }
11
12    digits.insert(0, 1);
13    return digits;
14  }
15}