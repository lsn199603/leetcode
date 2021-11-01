"""
给定两个字符串 text1 和 text2，返回这两个字符串的最长 公共子序列 的长度。如果不存在 公共子序列 ，返回 0 。

一个字符串的 子序列 是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。

例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。
两个字符串的 公共子序列 是这两个字符串所共同拥有的子序列。
输入：text1 = "abcde", text2 = "ace"
输出：3
解决办法：动态规划
"""
text1 = "abcde"
text2 = "aceed"
n1 = len(text1)
n2 = len(text2)

res = 0
# 创建动态规划表
dp = [[0 for _ in range(n2+1)] for _ in range(n1+1)]
# 在动态规划表中填值
for i in range(1, n1+1):
    for j in range(1, n2+1):
        # 如果xi=yj 且i,j>0 则是求解c[i-1,j-1]的最长子序列+1
        if text1[i-1] == text2[j - 1]:
            dp[i][j] = max(dp[i][j], dp[i-1][j-1] + 1)
            res = max(res, dp[i][j])
        # 如果xi!=yj max(dp[i-1][j], dp[i][j-1])
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
print(dp)

