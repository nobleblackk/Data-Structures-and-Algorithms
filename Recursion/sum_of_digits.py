import sys

sys.stdin = open("C:/Users/abhishek.sharma/Code/Zero/Data-Structures-and-Algorithms/input.txt", 'r')
sys.stdout = open("C:/Users/abhishek.sharma/Code/Zero/Data-Structures-and-Algorithms/output.txt", 'w')

# Find the sum of digits of a positive integer 

def sum_of_digits(n):
    # constraints
    assert n >= 0 and int(n) == n, "The number can not be negative and non-integer"

    # Base Case
    if n == 0:
        return 0 
    # Recursive Flow
    else: 
        return (n % 10) + sum_of_digits(n // 10)

print(sum_of_digits(int(float(input()))))