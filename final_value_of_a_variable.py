from typing import List


class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        count = 0
        for i in operations:
            if i == 'X++' or i == '++X':
                count += 1
            else:
                count -= 1
        return count

# Tests
# s = Solution()
# print(s.finalValueAfterOperations(["--X","X++","X++","X++","X++"]))