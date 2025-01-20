from util.testing import test_function

# Roman numerals consist of letters which represent numbers
# I is 1, V is 5, X is 10, L is 50, C is 100, D is 500, and M is 1000
# The actual value of roman numerals are all the letters added together. E.g II is 2, VI is 6, etc
# Unless a smaller roman numeral is before a bigger one, then you subtract it. E.g IV is 4 (V - I or 5 - 1).
# Another example: XXXIX is 39 (10 + 10 + 10 - 1 + 10  or X + X + X - I + X), subtracting I (1) because its before a bigger number
# See https://en.m.wikipedia.org/wiki/Roman_numerals#Standard_form for more information
def roman_numeral_to_number(roman_numerals):
    """
    Converts a string of roman numerals to a number

    Args:
        roman_numerals: A string of valid roman numerals, never empty. Consists of I, V, X, L, C, D, or M.

    Returns:
        A number
    """
    def numeral_to_number(numeral):
        match numeral:
            case "I":
                return 1
            case "V":
                return 5
            case "X":
                return 10
            case "L":
                return 50
            case "C":
                return 100
            case "D":
                return 500
            case "M":
                return 1000
    number = 0
    for i in range(0, len(roman_numerals)):
        if i == len(roman_numerals) - 1:
            number += numeral_to_number(roman_numerals[i])
            continue;
        if numeral_to_number(roman_numerals[i]) < numeral_to_number(roman_numerals[i+1]):
            number -= numeral_to_number(roman_numerals[i])
        else:
            number += numeral_to_number(roman_numerals[i])
    return number

    

print("Testing roman_numeral_to_number")
print("-------------------")
test_function(roman_numeral_to_number, 1, "I")
test_function(roman_numeral_to_number, 5, "V")
test_function(roman_numeral_to_number, 10, "X")
test_function(roman_numeral_to_number, 50, "L")
test_function(roman_numeral_to_number, 100, "C")
test_function(roman_numeral_to_number, 500, "D")
test_function(roman_numeral_to_number, 1000, "M")
test_function(roman_numeral_to_number, 1003, "MIII")
test_function(roman_numeral_to_number, 6, "VI")
test_function(roman_numeral_to_number, 110, "CX")
test_function(roman_numeral_to_number, 39, "XXXIX")
test_function(roman_numeral_to_number, 246, "CCXLVI")
test_function(roman_numeral_to_number, 789, "DCCLXXXIX")
test_function(roman_numeral_to_number, 2421, "MMCDXXI")
