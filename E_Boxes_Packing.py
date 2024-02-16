def min_visible_boxes(n, boxes):
    lis_lengths = [1] * n

    for i in range(1, n):
        for j in range(i):
            if boxes[i] < boxes[j]:
                lis_lengths[i] = max(lis_lengths[i], lis_lengths[j] + 1)

    return n - max(lis_lengths)

n = int(input())
boxes = list(map(int, input().split()))

print(min_visible_boxes(n, boxes))
