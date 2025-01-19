# Create a function get_primes(n), which takes in a number n and returns a list of prime numbers from 1 to n, inclusive of n. 1 is not prime.
# precondition: n >= 1
def get_primes(n):
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



def test_function(func, expected_output, *input):
    actual_output = func(*input)
    print(func.__name__ + '(', *input, ')')
    if actual_output == expected_output:
        print("Passed")
        print()
    else:
        print("FAILED")
        print("Expected output: ", expected_output)
        print("Actual output:   ", actual_output)
        print()

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
