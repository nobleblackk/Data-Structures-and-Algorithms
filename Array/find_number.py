import sys

sys.stdin = open("C:/Users/abhishek.sharma/Code/Zero/Data-Structures-and-Algorithms/input.txt", 'r')
sys.stdout = open("C:/Users/abhishek.sharma/Code/Zero/Data-Structures-and-Algorithms/output.txt", 'w')

def find_number(arr, number):
    for i in range(len(arr)):
        if arr[i] == number:
            return True
    return False

print(find_number([1,2], 2))