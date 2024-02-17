def quadruplet(n, target, values):
    for i in range(n):
        for j in range(i + 1, n):
            seen = set()
            for k in range(j + 1, n):
                complement = target - (values[i] + values[j] + values[k])
                if complement in seen:
                    for l in range(n):
                        if values[l] == complement and l != i and l != j and l != k:
                            return sorted([i + 1, j + 1, k + 1, l + 1])
                seen.add(values[k])
    return "IMPOSSIBLE"


n, target = map(int, input().split())
values = list(map(int, input().split()))

result = quadruplet(n, target, values)
if result == "IMPOSSIBLE":
    print(result)
else:
    print(*result)
