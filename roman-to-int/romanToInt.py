class Solution:

    roman = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    def romanToInt(self, s: str) -> int:
        summ = 0
        n = len(s)
        i = 0
        while i < n:
            if i < n - 1 and self.roman[s[i + 1]] > self.roman[s[i]]:
                summ += self.roman[s[i + 1]] - self.roman[s[i]]
                i += 2
            else:
                summ += self.roman[s[i]]
                i += 1
        return summ


if __name__ == "__main__":
    sol = Solution()
    print(f"sol.romanToInt('II')      => {sol.romanToInt('II')}")
    print(f"sol.romanToInt('XXVII')   => {sol.romanToInt('XXVII')}")
    print(f"sol.romanToInt('MCMXCIV') => {sol.romanToInt('MCMXCIV')}")
