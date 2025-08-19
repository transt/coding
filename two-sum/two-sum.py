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
    print(f"([2, 7, 11, 15], 9)  => {sol.twoSum([2,7,11,15], 9)}")
    print(f"([3, 2, 4], 6)       => {sol.twoSum([3,2,4], 6)}")
    print(f"([3,3], 6)           => {sol.twoSum([3,3], 6)}")
    print(f"([1, 4, 6, 2], 7)    => {sol.twoSum([1, 4, 6, 2], 7)}")
    print(f"([1, 4, 6, 2], 0)    => {sol.twoSum([1, 4, 6, 2], 0)}")
