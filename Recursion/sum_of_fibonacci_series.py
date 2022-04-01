import sys

sys.stdin = open("C:/Users/abhishek.sharma/Code/Zero/Data-Structures-and-Algorithms/input.txt", 'r')
sys.stdout = open("C:/Users/abhishek.sharma/Code/Zero/Data-Structures-and-Algorithms/output.txt", 'w')

# Find the sum of fibonacci series
# Sum of fibonacci series can be computed as:
# sum(n) = f(n+2) - 1

def sum_of_fibonacci_series_utility(n):
    # Base case
    if n in [1,2]:
        return n - 1
    # Recursive flow
    else: 
        return sum_of_fibonacci_series_utility(n-1) + sum_of_fibonacci_series_utility(n-2)


def sum_of_fibonacci_series(n):
    # Constraints
    assert n > 0 and int(n) == n, "Fibonacci number can not be negative or non-integer"

    return sum_of_fibonacci_series_utility(n+2) - 1

print(sum_of_fibonacci_series(7))