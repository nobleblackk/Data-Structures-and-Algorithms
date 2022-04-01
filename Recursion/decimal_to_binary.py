import sys

sys.stdin = open("C:/Users/abhishek.sharma/Code/Zero/Data-Structures-and-Algorithms/input.txt", 'r')
sys.stdout = open("C:/Users/abhishek.sharma/Code/Zero/Data-Structures-and-Algorithms/output.txt", 'w')

# Conver decimal number to binary number
# e.g. 13 -> 1101
# Remainder of n + function_call(n//1)

def decimal_to_binary(n):
    # Constraints
    assert n >= 0 and int(n) == n, "The number can not be negative and non-integer"

    # Base case
    if n in [0, 1]:
        return n
    # Recursive flow
    else:
        return n % 2 + decimal_to_binary(n//2) * 10

print(decimal_to_binary(6))