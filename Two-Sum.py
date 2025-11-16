# # question - Given an array of integers nums and an integer target, return the indices of the two numbers such that they add up to target.
# You may assume exactly one solution exists, and you may not use the same element twice. Return indices in any order.


nums = input().strip("[]").split(",")
nums = list(map(int, nums))
target = int(input())

def twoSum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return [seen[diff], i]
        seen[num] = i   
        
print(twoSum(nums, target))

# class Solution:
#     def twoSum(self, nums, target):
#         seen = {}
#         for i, num in enumerate(nums):
#             diff = target - num
#             if diff in seen:
#                 return [seen[diff], i]
#             seen[num] = i

# # input
# nums = list(map(int, input().split()))
# target = int(input())

# print(Solution().twoSum(nums, target))

