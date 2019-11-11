'''
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
Note: The solution set must not contain duplicate triplets.

Example:
Given array nums = [-1, 0, 1, 2, -1, -4],
A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''

# #3 - the most fastest
import operator

def threeSum(self, nums: List[int]) -> List[List[int]]:
    result = []
    if len(nums) < 3:
        return []
    if all(num == 0 for num in nums):
        return [[0, 0, 0]]
    nums.sort()
    for i in range(1, len(nums) - 1):
        i_sum = 0 - nums[i]
        left = 0
        right = len(nums) - 1
        while left < i < right:
            two_sum = nums[left] + nums[right]
            if two_sum == i_sum:
                result.append([nums[left], nums[i], nums[right]])
                left += 1
            elif two_sum < i_sum:
                left += 1
            elif two_sum > i_sum:
                right -= 1
    result_unique = []
    if result:
        result.sort(key=operator.itemgetter(0))
        for j in range(len(result) - 1):
            if result[j] != result[j + 1]:
                result_unique.append(result[j])
        result_unique.append(result[-1])
    return result_unique


nums = [-1, 0, 1, 2, -1, -4]
res = threeSum(nums)
print(res)                      # [[-1,-1,2],[-1,0,1]]

# #2 - more memory
def threeSum(self, nums: List[int]) -> List[List[int]]:
    result = []
    unique = []
    nums.sort()
    for i in range(1, len(nums)-1):
        i_sum = 0 - nums[i]
        left = 0
        right = len(nums) - 1
        while left < i  and i < right:
            two_sum = nums[left] + nums[right]
            if two_sum == i_sum:
                if {nums[left], nums[i], nums[right]} not in unique:
                    result.append([nums[left], nums[i], nums[right]])
                    unique.append({nums[left], nums[i], nums[right]})
                left += 1
            elif two_sum < i_sum:
                left += 1
            elif two_sum > i_sum:
                right -= 1

    return result

# #1 - more time
def threeSum(self, nums: List[int]) -> List[List[int]]:
    result = []
    unique_sets = []

    for i in range(len(nums)):
        i_sum = 0 - nums[i]
        for j in range(i + 1, len(nums)):

            k = 0 - nums[i] - nums[j]
            if k in nums[j + 1:] and {nums[i], nums[j], k} not in unique_sets:
                result.append([nums[i], nums[j], k])
                unique_sets.append({nums[i], nums[j], k})

    return result
