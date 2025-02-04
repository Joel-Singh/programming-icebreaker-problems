# programming-contest-for-club
A bank of problems for icebreakers or programming contest

There are problems in the problems/ directory. Each problem is formatted like so:

```
from util.testing import test_function

def get_primes(n):
    """
    Returns a list of prime numbers from 1 to n, inclusive of n. 1 is not prime

    Args:
        n: The number to find primes up to, will be >= 1

    Returns:
        A list of prime numbers from 1 to n
    """
    primes = []
    for potential_prime in range(2, n+1):
        is_prime = True
        for divisor in range(2, potential_prime):
            if (potential_prime%divisor) == 0:
                is_prime = False
                break;
        if is_prime:
            primes.append(potential_prime)
    return primes

print("Testing get_primes")
print("-------------------")
test_function(get_primes, [], 1)
test_function(get_primes, [2], 2)
test_function(get_primes, [2, 3], 3)
test_function(get_primes, [2, 3, 5], 5)
test_function(get_primes, [2, 3, 5, 7], 7)
test_function(get_primes, [2, 3, 5, 7], 8)
test_function(get_primes, [2, 3, 5, 7, 11], 11)
test_function(get_primes, [2, 3, 5, 7, 11], 12)
test_function(get_primes, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73], 73)
test_function(get_primes, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73], 78)
test_function(get_primes, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107], 107)
```

- Each file imports test_function, which prints whether or not the test passed, taking in expected output.
- The solution will obviously not be there for the final contest
- The intention is for members to be constantly running tests as incrementally work towards a final solution
