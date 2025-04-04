# programming-icebreaker-problems
A bank of problems for icebreakers during meetings at Denison

The current problems for the meeting are on the main branch. All other problems and solutions are on all-solutions-and-problems.

```python
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
    # Calculate and append primes to list
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
- The intention is for members to be constantly running tests as they incrementally work towards a final solution

Example output after running the file would look like:
```
get_primes( 1 )
Passed

get_primes( 2 )
FAILED
Expected output: [2]
Actual output:    []

get_primes( 3 )
FAILED
Expected output: [2, 3]
Actual output:    [2]

get_primes( 5 )
FAILED
Expected output: [2, 3, 5]
Actual output:    [2, 3]

get_primes( 7 )
FAILED
Expected output: [2, 3, 5, 7]
Actual output:    [2, 3, 5]

get_primes( 8 )
Passed
```
