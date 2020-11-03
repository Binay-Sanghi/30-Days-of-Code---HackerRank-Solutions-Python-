mat = []
for i in range(6):
    mat.append(list(map(int, input().split())))
max_sum = -100
for i in range(4):
    for j in range(4):
        temp_sum = mat[i][j] + mat[i][j+1] + mat[i][j+2] + mat[i+1][j+1] + mat[i+2][j] + mat[i+2][j+1] + mat[i+2][j+2]
        max_sum = max(max_sum,temp_sum)
print(max_sum)
