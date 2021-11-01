"""
给定一个 n × n 的二维矩阵 matrix 表示一个图像。请你将图像顺时针旋转 90 度。

你必须在 原地 旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要 使用另一个矩阵来旋转图像
输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[[7,4,1],[8,5,2],[9,6,3]]
"""
matrix = [[1,2,3],[4,5,6],[7,8,9]]
n = len(matrix)
# # 主对角线反转
# for i in range(n):
#     for j in range(i):
#         matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
# # 水平先反转
# print(matrix)
# for i in range(n):
#     matrix[i].reverse()
n = len(matrix)
for i in range(n // 2):
    for j in range(i, n-1-i):
        print(i)
        print(j)
        matrix[i][j], matrix[n - j - 1][i], matrix[n - i - 1][n - j - 1], matrix[j][n - i - 1] \
            = matrix[n - j - 1][i], matrix[n - i - 1][n - j - 1], matrix[j][n - i - 1], matrix[i][j]

print(matrix)