# Last updated: 30/09/2026, 08:26:43
1class Solution:
2    def tribonacci(self, n: int) -> int:
3        a = 0  # Initialize the first term of the sequence
4        b = 1  # Initialize the second term of the sequence
5        c = 1  # Initialize the third term of the sequence
6        if n == 0:
7            return 0  # If n is 0, return the first term
8        if n == 1 or n == 2:
9            return 1  # If n is 1 or 2, return the second or third term respectively
10        for i in range(3, n+1):  # Start the loop from the third term
11            d = a + b + c  # Calculate the next term in the sequence
12            a = b  # Update the value of a
13            b = c  # Update the value of b
14            c = d  # Update the value of c
15        return d  # Return the nth term