n = int(input())
d = {}
for i in range(n):
    a,b = map(str, input().split())
    d[a] = b
temp = True
while(True):
    try:
        x = str(input())
        if (x in d):
            print(x + "=" + d[x])
        else:
            print("Not found")
    except EOFError:
        break
