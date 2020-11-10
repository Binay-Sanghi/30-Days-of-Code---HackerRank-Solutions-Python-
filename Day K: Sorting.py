n = int(input())
a = list(map(int,input().split()))
numberOfSwaps = 0
for i in range(0,n):
    for j in range(0,n-1):
        if (a[j] > a[j+1]):
            a[j],a[j+1] = a[j+1],a[j]
            numberOfSwaps+=1
print("Array is sorted in " + str(numberOfSwaps) + " swaps.")
print("First Element: " + str(a[0]))
print("Last Element: " + str(a[-1]))
