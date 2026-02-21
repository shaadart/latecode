# Last updated: 2/21/2026, 2:49:10 PM
1
2#First Solution 
3# class Solution:
4#     def countPrimeSetBits(self, left: int, right: int) -> int:
5#         def isPrime(n):
6#             return (all(False for i in range(2,n) if n % i == 0) and not n < 2)
7
8#         count = 0
9#         for i in range(left, right+1):
10#             bitCount = int(bin(i).count('1'))
11#             print(i, bitCount, isPrime(i), count)
12#             if isPrime(bitCount):
13#                 count= count+1
14
15#         return count
16
17
18class Solution:
19    def countPrimeSetBits(self, left: int, right: int) -> int:
20        # def isPrime(n):
21        #     return (all(False for i in range(2,n) if n % i == 0) and not n < 2)
22
23        primes = {2, 3, 5, 7, 11, 13, 17, 19}
24        count = 0
25        for i in range(left, right+1):
26            bitCount = int(bin(i).count('1'))
27           
28            if (bitCount in primes):
29                count= count+1
30
31        return count
32
33
34
35