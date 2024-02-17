if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    s_array = sorted(arr)
    for i in range(1, n + 1):
      if s_array[i] != s_array[-1]:
        print(s_array[i])
      