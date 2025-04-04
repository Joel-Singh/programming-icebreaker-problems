from util.testing import test_function

def get_primes(n):
    """
    Returns a list of prime numbers from 1 to n, inclusive of n. 1 is not prime

    Args:
        n: The number to find primes up to, will be >= 1

    Returns:
        A list of prime numbers from 1 to n
    """
    return []


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
