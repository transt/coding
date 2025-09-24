"""
Given an array of integers nums and an integer target, return indices of 
the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and 
you may not use the same element twice.

You can return the answer in any order.
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, val in enumerate(nums):
            complement = target - val
            if complement in seen:
                return [seen[complement], i]
            seen[val] = i
        return []


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3,3], 6, [0, 1]),
        ([1, 4, 6, 2], 7, [0, 2]),
        ([1, 4, 6, 2], 0, [])
    ]

    for i, (nums, target, expected) in enumerate(tests, 1):
        result = sol.twoSum(nums, target)
        print(f"Test {i}: twoSum({nums}, {target}) => result={result}, expected={expected}")
        assert result == expected, f"Test {i} failed! Expected={expected}, got={result}"
    print("All tests passed!")
