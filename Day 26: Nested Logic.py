a = list(map(int,input().split()))
e = list(map(int,input().split()))
if (a[2],a[1],a[0]) <= (e[2],e[1],e[0]):
    print(0)
elif (a[2],a[1]) == (e[2],e[1]):
    print(15*(a[0]-e[0]))
elif (a[2] == e[2]):  
    print(500*(a[1]-e[1]))
else:
    print(10000) 
