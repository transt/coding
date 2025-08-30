from typing import List


class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        closest = nums[0]
        for x in nums:
            if abs(x) < abs(closest):
                closest = x
        if closest < 0 and abs(closest) in nums:
            return abs(closest)
        return closest

        # Time: O(n)
        # Space: O(1)


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([-4, -2, 1, 4, 8], 1),
        ([-4, -2, -1, 4, 8], -1),
        ([2, -1, 1], 1)
    ]

    for i, (arg, expected) in enumerate(tests, 1):
        result = sol.findClosestNumber(arg)
        print(f"Test {i}: findClosestNumber({arg}) => result={result}, expected={expected}")
        assert result == expected, f"Test {i} failed! Expected={expected}, got={result}"
    print("All tests passed!")
