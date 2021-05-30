''' Count the number of prime numbers less than a non-negative number, n.

Example 1:

Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7. '''

import math
class Solution:
    def countPrimes(self, n: int) -> int:
        if (n < 2):
            return 0
        
        # assuming all numbers are prime
        isPrime = [True] * n
        # assigning false to 0 and 1 as they are not prime numbers
        isPrime[0] = isPrime[1] = False
        # looping from 2 to sqrt(N) to find primes
        for i in range(2, math.ceil(math.sqrt(n))):
            # if the number is prime 
            if(isPrime[i]):
                # then the multiples of num are not prime so make them false 
                # so we start from square of a num till n, in steps of given num
                for multiples_of_i in range(i*i, n, i):
                    isPrime[multiples_of_i] = False

        # returning the count of prime numbers
        return sum(isPrime)

s = Solution()
ans = s.countPrimes(100)
print(f"The number of prime numbers less than given number are {ans}.")
