def running_miles(t, tests):
    for b in tests:
        n = len(b)
        max_sum = float('-inf')
        for i in range(n - 2):
            for j in range(i + 2, n):
                top_b = sorted(b[i:j + 1], reverse=True)[:3]
                b_sum = sum(top_b) - (j - i)
                max_sum = max(max_sum, b_sum)
        print(max_sum)

t = int(input())
tests = []
for _ in range(t):
    n = int(input())
    b = list(map(int, input().split()))
    tests.append(b)

running_miles(t, tests)
