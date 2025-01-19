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
