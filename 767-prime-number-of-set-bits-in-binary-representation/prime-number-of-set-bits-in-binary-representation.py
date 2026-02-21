
#First Solution 
# class Solution:
#     def countPrimeSetBits(self, left: int, right: int) -> int:
#         def isPrime(n):
#             return (all(False for i in range(2,n) if n % i == 0) and not n < 2)

#         count = 0
#         for i in range(left, right+1):
#             bitCount = int(bin(i).count('1'))
#             print(i, bitCount, isPrime(i), count)
#             if isPrime(bitCount):
#                 count= count+1

#         return count


class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        # def isPrime(n):
        #     return (all(False for i in range(2,n) if n % i == 0) and not n < 2)

        primes = {2, 3, 5, 7, 11, 13, 17, 19}
        count = 0
        for i in range(left, right+1):
            bitCount = int(bin(i).count('1'))
           
            if (bitCount in primes):
                count= count+1

        return count



