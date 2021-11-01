"""
给定一个字符串 s 和一个字符串 t ，计算在 s 的子序列中 t 出现的个数。

字符串的一个 子序列 是指，通过删除一些（也可以不删除）字符且不干扰剩余字符相对位置所组成的新字符串。（例如，"ACE" 是 "ABCDE" 的一个子序列，而 "AEC" 不是）

题目数据保证答案符合 32 位带符号整数范围。

"""
s = "rabbbit"
t = "rabbit"
length_s = len(s)
length_t = len(t)
# 1. 创建dp数组及下标的含义 DP数组初始化
dp = [[0] * (length_s+1) for _ in range(length_t+1)]
print(dp)
# 2. 确定遍历顺序
for i in range(1, length_t+1):
    for j in range(1, length_s+1):
        if s[j-1] == t[i-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = dp[i][j-1]
print(dp)
# if dp[-1][-1] == length_s:
#     print(True)
# else:
#     print(False)