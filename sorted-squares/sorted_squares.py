"""
Given an integer array nums sorted in non-decreasing order, return
an array of the squares of each number sorted in non-decreasing order.
"""

from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        result = []
        while left <= right:
            if abs(nums[left]) < abs(nums[right]):
                result.append(nums[right] ** 2)
                right -= 1
            else:
                result.append(nums[left] ** 2)
                left += 1
        result.reverse()
        return result

if __name__ == "__main__":
    sol = Solution()
    print(f"[-4, -2, 0, 1, 4, 10] => {sol.sortedSquares([-4, -2, 0, 1, 4, 10])}")
    print(f"[-7, -3, 2, 3, 11]    => {sol.sortedSquares([-7, -3, 2, 3, 11])}")
