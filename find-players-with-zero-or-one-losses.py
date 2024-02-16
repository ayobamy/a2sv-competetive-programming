import collections
from typing import List

class Solution:
  def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
    ans = [[] for _ in range(2)]
    countLosses = collections.Counter()

    for winner, loser in matches:
      if winner not in countLosses:
        countLosses[winner] = 0
      countLosses[loser] += 1

    for player, losses in countLosses.items():
      if losses < 2:
        ans[losses].append(player)

    return [sorted(ans[0]), sorted(ans[1])]

# Tests
sol = Solution()
print(sol.findWinners([[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]))
