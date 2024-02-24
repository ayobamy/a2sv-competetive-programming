n = int(input())
arr = list(map(int, input().split()))

def array_division(n, arr):
    neg = [i for i in arr if i < 0]
    pos = [i for i in arr if i > 0]
    zero = [i for i in arr if i == 0]

    if not pos:
        pos.append(neg.pop())
        pos.append(neg.pop())
    
    if not neg:
        neg.append(pos.pop())
    
    print(len(neg), *neg)
    print(len(pos), *pos)
    print(len(zero), *zero)

array_division(n, arr)
