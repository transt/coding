from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero_count = 0
        zero_index = None
        n = len(nums)
        for i, num in enumerate(nums):
            if num == 0:
                zero_count += 1
                if zero_count == 1:
                    zero_index = i
                else:
                    break
            else:
                product *= num

        if zero_count == 1:
            result = [0] * n 
            result[zero_index] = product
            return result
        if zero_count > 1:
            return [0] * n
        return [product // num for num in nums]


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([1, 2, 3, 4], [24, 12, 8, 6]),
        ([-1, 1, 0, -3, 3], [0, 0, 9, 0, 0]),
        ([1, 2, 0, 0], [0, 0, 0, 0])
    ]

    for i, (arg, expected) in enumerate(tests, 1):
        result = sol.productExceptSelf(arg)
        print(f"Test {i}, productExceptSelf({arg}) => result={result}, expected={expected}")
        assert result == expected, f"Test {i} failed!, expected={expected}, got={result}"
    print("All tests passed!")
