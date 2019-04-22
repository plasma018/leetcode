#Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

# Follow-up: what if you can't use division?

def solution(A):
    l = len(A)
    right = [1] * l 
    left = [1] * l
    answer = [0] * l

    for i in range(1,l):
        right[i] = right[i-1]*A[i-1]
    
    for i in range(l-2,-1,-1):
        left[i] = left[i+1]*A[i+1]

    for i in range(l):
        answer[i] = left[i]*right[i]
    print('r',right)
    print('l',left)
    return answer

print(solution([3,2,1]))