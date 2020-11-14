t = int(input())
for i in range(t):
    n = int(input())
    if(n==1):
        print("Not prime")    
    else:
        k = int(n**0.5)
        ans = "Prime"
        for j in range(2,k+1):
            if (n%j==0):
                ans = "Not prime"
                break
        print(ans)
