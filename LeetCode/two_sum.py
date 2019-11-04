# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

class Solution:
    @classmethod
    def twoSum(cls, nums, target):
        addition_sum = {}
        for i, n in enumerate(nums):
            if n in addition_sum:
                return [addition_sum[n], i]
                break
            else:
                addition_sum[target - n] = i

        return []

s = Solution()
nums = [2, 6, 11, 7, 15]
target = 9
result = s.twoSum(nums=nums, target=target)
print(result) # result = [0, 3]