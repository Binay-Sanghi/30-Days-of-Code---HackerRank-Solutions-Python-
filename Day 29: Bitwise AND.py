n = int(input())
for i in range(n):
    n,k = map(int, input().split())
    if((k-1)|k <= n):
        print(k-1)
    else:
        print(k-2)
