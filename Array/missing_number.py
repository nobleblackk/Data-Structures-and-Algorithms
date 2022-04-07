import sys

sys.stdin = open("C:/Users/abhishek.sharma/Code/Zero/Data-Structures-and-Algorithms/input.txt", 'r')
sys.stdout = open("C:/Users/abhishek.sharma/Code/Zero/Data-Structures-and-Algorithms/output.txt", 'w')


def missing_number(arr):
    # Constraints 
    if len(arr) == 0:
         return 0 
    else:
        n = len(arr) + 1 
        sum1 = (n*(n+1))//2
        sum2 = sum(arr) 
        return sum1 - sum2 

print(missing_number([1,2,3,4])) 