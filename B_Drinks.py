def drinks_fraction(n, percents):
    total = sum(percents)
    avg = total / n

    return avg

n = int(input())
percents = list(map(int, input().split()))

result = drinks_fraction(n, percents)
result_str = "{:.12f}".format(result)

print(result_str)
