from typing import List


class Solution:
    def mergeInterval(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        output = []
        for interval in intervals:
            if not output:
                output.append(interval)
            else:
                value = output[-1]
                if interval[0] <= value[1]:
                    value[1] = max(interval[1], value[1])
                else:
                    output.append(interval)
        return output


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]]),
        ([[1, 4], [4, 5]], [[1,5]])
    ]

    for idx, (arg, expected) in enumerate(tests, 1):
        result = sol.mergeInterval(arg)
        print(f"Test {idx}: mergeInterval({arg}) => result={result}, expected={expected}")
        assert result == expected, f"Test {idx} failed: expected={expected}, got={result}"

    print("All tests passed!")
