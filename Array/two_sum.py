import sys

sys.stdin = open("C:/Users/abhishek.sharma/Code/Zero/Data-Structures-and-Algorithms/input.txt", 'r')
sys.stdout = open("C:/Users/abhishek.sharma/Code/Zero/Data-Structures-and-Algorithms/output.txt", 'w')

# using hash map 
def two_sum(arr, target):
    seen = {} 
    for i in range(len(arr)):
        remaining = target - arr[i]
        if remaining in seen:
            return [i, seen[remaining]]
        else:
            seen[arr[i]] = i 

print(two_sum([1,2,3,4,5,6], 9))
