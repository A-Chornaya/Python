'''
Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.
Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
Note: You are not suppose to use the library's sort function for this problem.

Example:
Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
'''

from collections import Counter

# return new list
def sortColors(nums):
    c = Counter(nums)
    return [0]*c[0] + [1]*c[1] + [2]*c[2]

# rewrite source list
def sortColors2(nums):
    c = Counter(nums)
    nums.clear()
    nums.extend([0]*c[0] + [1]*c[1] + [2]*c[2])

# sort in the same list
def sortColors3(nums):
    i = 0
    end = len(nums)
    j = end
    next = 0
    while next < j:
        current = nums.pop(next)
        if current == 2:
            nums.insert(end, current)
            j -= 1
        elif current == 1:
            nums.insert(i, current)
            next += 1
        else:
            nums.insert(0, current)
            i += 1
            next += 1

n = [2,0,2,1,1,0]
n2 = sortColors(n)
print(n2)
# [0, 0, 1, 1, 2, 2]

n = [2,0,2,1,1,0]
sortColors2(n)
print(n)
# [0, 0, 1, 1, 2, 2]

n = [2,0,1,2,0,1,1,1,0,2,0]
sortColors3(n)
print(n)
# [0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2]