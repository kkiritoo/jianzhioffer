#输入指定大小的数组
M = int(input())  # 行
N = int(input())  # 列
A = [[0]*N] * M  # 初始化二维矩阵
for i in range(M):  # 从键盘输入矩阵
    A[i] = input().split(" ")
    A[i] = [int(j) for j in A[i]]
    '''
    此处还有第二种写法,可将A[i]=[int(j) for j in A[i]]替换为:
    for j in range(N):
        A[i][j]=int(A[i][j])
    '''
 
print(A)