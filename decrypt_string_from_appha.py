class Solution:
    def freqAlphabets(self, s: str) -> str:
        i = len(s) - 1
        res = ""
        while i >= 0:
            if s[i] == '#':
                num = int(s[i-2:i])
                res = chr(num + 96) + res
                i -= 3
            else:
                res = chr(int(s[i]) + 96) + res
                i -= 1
        return res

# Tests
sol = Solution()
print(sol.freqAlphabets("10#11#12"))