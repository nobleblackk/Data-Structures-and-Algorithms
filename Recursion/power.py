import sys

sys.stdin = open("C:/Users/abhishek.sharma/Code/Zero/Data-Structures-and-Algorithms/input.txt", 'r')
sys.stdout = open("C:/Users/abhishek.sharma/Code/Zero/Data-Structures-and-Algorithms/output.txt", 'w')

# Find the power of a number 

def power(base, exp):
    # Constraints
    assert base > 0 and exp >= 0 and int(exp) == exp, "Base should always be a positive number. Exponential should always be a positive number and  can not be non-integer"

    # Base Case 
    if (exp == 0):
        return 1 
    # Recursive Flow 
    else:
        return base * power(base, exp - 1)

a, b = (map(lambda x : int(x), input().split()))
print(power(a,b))