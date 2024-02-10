class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        char_count = {}
    
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
        
        for char in t:
            if char_count.get(char, 0) == 0:
                return char
            else:
                char_count[char] -= 1

        return ""
# Tests
# sol = Solution()

# s = "abcd"
# t = "abcde"

# print(sol.findTheDifference(s, t))
