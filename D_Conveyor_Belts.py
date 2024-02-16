import math

def min_energy(n, x1, y1, x2, y2):
    x = abs(x2 - x1)
    y = abs(y2 - y1)
    
    min_x = min(x, n - x)
    min_y = min(y, n - y)
    
    return min_x + min_y

# Read the number of test cases
t = int(input())
for _ in range(t):
    n, x1, y1, x2, y2 = map(int, input().split())

    print(min_energy(n, x1, y1, x2, y2))
