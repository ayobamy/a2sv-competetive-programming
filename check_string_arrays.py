from typing import List


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        if ''.join(word1) == ''.join(word2):
            return True
        return False

# # Tests
sol = Solution()  
word1 = ["ab", "c"]
word2 = ["a", "bc"]

result = print(sol.arrayStringsAreEqual(word1, word2))

                