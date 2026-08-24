class Solution:
    def prime_Sum(self, n: int) -> int:
        prime_sum = 0
    
        # Check every number from 2 up to n
        for num in range(2, n + 1):
    
            # Check if 'num' has any factors up to its square root
            is_prime = True
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    is_prime = False  # Found a factor, not prime
                    break             # Stop checking this number immediately
    
            # If no factors were found, add it to our total
            if is_prime:
                prime_sum += num
    
        return prime_sum
