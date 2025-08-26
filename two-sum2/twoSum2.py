"""
Given a 1-indexed array of integers num that is already sorted in non-decreasing order,
find two numbers such taht they add up to a specific target number.
"""

from typing import List


class Solution:
    def twoSum2(self, num: List[int], target: int) -> List[int]:
        n = len(num)
        l = 0
        r = n - 1
        while l < r:
            summ = num[l] + num[r]
            if summ == target:
                return [l + 1, r + 1]

            if summ < target:
                l += 1
            else:
                r -= 1


if __name__ == "__main__":
    sol = Solution()
    print(f"[2, 7, 11, 15], 9          => {sol.twoSum2([2, 7, 11, 15], 9)}")
    print(f"[1, 5, 10, 11, 15, 25], 21 => {sol.twoSum2([1, 5, 10, 11, 15, 25], 21)}")
    print(f"[2, 3, 4], 6               => {sol.twoSum2([2, 3, 4], 6)}")
