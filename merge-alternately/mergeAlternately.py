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
    print(f"mergeAlternately('abc', 'pqr')   => {sol.mergeAlternately('abc', 'pqr')}")
    print(f"mergeAlternately('abc', 'pqrst') => {sol.mergeAlternately('abc', 'pqrst')}")
