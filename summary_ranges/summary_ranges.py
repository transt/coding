from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        n = len(nums)
        start = nums[0]
        end = nums[0]
        ans = []
        for i in range(n):
            if i < n - 1 and nums[i + 1] == end + 1:
                end += 1
            elif i < n - 1 and nums[i + 1] != end + 1:
                if start == end:
                    ans.append(str(start))
                else:
                    ans.append(str(start) + "->" + str(end))
                start = nums[i + 1]
                end = start
        if start == end:
            ans.append(str(start))
        else:
            ans.append(f"{start}->{end}")
        return ans


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([0, 1, 2, 4, 5, 7], ["0->2", "4->5", "7"]),
        ([0, 2, 3, 4, 6, 8, 9], ["0", "2->4", "6", "8->9"])
    ]

    for i, (arg, expected) in enumerate(tests, 1):
        result = sol.summaryRanges(arg)
        print(f"Test {i}: summaryRanges({arg}) => result={result}, expected={expected}")
        assert result == expected, f"Test {i} failed! Expected={expected}, got={result}"

    print("All Tests passed!")
