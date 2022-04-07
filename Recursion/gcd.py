import sys

sys.stdin = open("C:/Users/abhishek.sharma/Code/Zero/Data-Structures-and-Algorithms/input.txt", 'r')
sys.stdout = open("C:/Users/abhishek.sharma/Code/Zero/Data-Structures-and-Algorithms/output.txt", 'w')


# Euclidean Algorithm: divide by the small number then in the next 
# iteration, remainder becomes the small number 

def gcd(a, b):
    # constraints
    assert a >= 0 and b >= 0 and int(a) == a and int(b) == b, "GCD numbers can not be negative or non-integer"

    # Base case
    if (b == 0):
        return a 
    # Recursive flow
    else: 
        return gcd(b, a%b)

print(gcd(48, 31))