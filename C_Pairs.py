from collections import defaultdict

def pairs(n, a, b, c):
    count = defaultdict(int)
    for elem in c:
        count[elem] += 1

    pairs_count = 0
    for ai in a:
        for bj in b:
            if ai == bj * count[ai]:
                pairs_count += count[ai]

    return pairs_count

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

res = pairs(n, a, b, c)
print(res)
