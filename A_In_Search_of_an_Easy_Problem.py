def check_difficulty(n, options):
    if 1 in options:
        print("HARD")
    else:
        print("EASY")

n = int(input())
options = list(map(int, input().split()))

check_difficulty(n, options)
