"""
给两个整数数组 A 和 B ，返回两个数组中公共的、长度最长的子数组的长度。
示例：
输入：
A: [1,2,3,2,1]
B: [3,2,1,4,7]
输出：3
解释：
长度最长的公共子数组是 [3, 2, 1]
1. 确定dp数组以及下标的含义
dp[i][j]：以下标i - 1为结尾的A，和以下标j - 1为结尾的B，最长重复子数组长度为dp[i][j]
"""
A = [1, 2, 3, 2, 1]
B = [3, 2, 1, 4, 7]
length_A = len(A)
length_B = len(B)

# 1.创建dp数组
dp = [[0] * (length_A+1) for _ in range(length_B+1)]
result = 0
# 对dp数组赋值
for i in range(1, length_B+1):
    for j in range(1, length_A+1):
        if B[i-1] == A[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        result = max(result, dp[i][j])
print(result)
