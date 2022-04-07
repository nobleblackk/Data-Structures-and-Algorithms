import sys

sys.stdin = open("C:/Users/abhishek.sharma/Code/Zero/Data-Structures-and-Algorithms/input.txt", 'r')
sys.stdout = open("C:/Users/abhishek.sharma/Code/Zero/Data-Structures-and-Algorithms/output.txt", 'w')

def is_unique(arr):
    set1 = set() 
    for i in range(len(arr)):
        if arr[i] in set1:
            return "Not Unique"
        else:
            set1.add(arr[i])
    return "Unique"

print(is_unique([1,2,3,4,5,4]))