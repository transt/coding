class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len1 = len(word1)
        len2 = len(word2)
        new_word = []
        for i in range(min(len1, len2)):
            new_word.append(word1[i])
            new_word.append(word2[i])
        if len1 < len2:
            new_word.append(word2[len1:])
        elif len1 > len2:
            new_word.append(word1[len2:])
        return "".join(new_word)

                            
if __name__ == "__main__":
    sol = Solution()
    tests = [
        ('abc', 'pqr', 'apbqcr'),
        ('ab', 'pqrs', 'apbqrs'),
        ('abcd', 'pq', 'apbqcd')
    ]

    for i, (word1, word2, expected) in enumerate(tests, 1):
        result = sol.mergeAlternately(word1, word2)
        print(f"Test {i}: mergeAlternately({word1}, {word2}) => result={result}, expected={expected}")
        assert result == expected, f"Test {i} failed! Expected={expected}, got={result}"
    print("All tests passed!")
