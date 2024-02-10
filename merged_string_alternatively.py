class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged_str = ''
        len1 = len(word1)
        len2 = len(word2)
        
        len_max = max(len1, len2)

        for i in range(len_max):
            if i < len1:
                merged_str += word1[i]
            if i < len2:
                merged_str += word2[i]
        return merged_str

# Tests
# sol = Solution()

# word1 = "abc"
# word2 = "pqrt"

# print(sol.mergeAlternately(word1, word2))