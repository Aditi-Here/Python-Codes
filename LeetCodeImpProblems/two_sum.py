"""
Question:
Given an array of integers, find two numbers such that they add up to
a specific target number.
The function twoSum should return indices of the two numbers such that
they add up to the target, where index1 must be less than index2.
Please note that your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution.
O(n) runtime, O(n) space – Hash table:
We could reduce the runtime complexity of looking up a value to O(1) using a hash map
that maps a value to its index.
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for n in range(len(nums)):
            diff=target-nums[n]
            if diff in nums and nums.index(diff)!=n:
                return [n,nums.index(diff)]