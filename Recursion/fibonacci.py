import sys 

sys.stdin = open("C:/Users/abhishek.sharma/Code/Zero/Data-Structures-and-Algorithms/input.txt", 'r')
sys.stdout = open("C:/Users/abhishek.sharma/Code/Zero/Data-Structures-and-Algorithms/output.txt", 'w')

# Fibonacci number: It is the sequence of numbers where each number is the sum of preceeding two numbers
# and it starts from 0 and 1. 

def fibonacci(n):
    assert n > 0 and int(n) == n, "Fibonacci number can not be negative or non-integer"
    if n in [1,2]:
        return n-1  
    else:
        return fibonacci(n-1) + fibonacci(n-2) 


