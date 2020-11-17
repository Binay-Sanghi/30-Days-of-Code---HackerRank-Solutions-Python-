n = int(input())
name = []
email = []
for i in range(n):
    a,b = map(str,input().split())
    name.append(a)
    email.append(b)
ans = []
for i in range(n):
    if(email[i].endswith("@gmail.com")):
        ans.append(name[i])
ans.sort()
for i in range(len(ans)):
    print(ans[i]) 
