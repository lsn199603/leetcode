"""
给定两个字符串 text1 和 text2，返回这两个字符串的最长 公共子序列 的长度。如果不存在 公共子序列 ，返回 0 。
一个字符串的 子序列 是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。
例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。
两个字符串的 公共子序列 是这两个字符串所共同拥有的子序列。
示例 1：
输入：text1 = "abcde", text2 = "ace"
输出：3
解释：最长公共子序列是 "ace" ，它的长度为 3 。
1. 确定dp数组以及下标的含义
dp[i][j]：长度为[0,i-1]的字符串text1与长度为[0,j-1]的字符串text2的最长公共子序列为dp[i][j]
2. 确定递推公式
    a.text[i-1] 与 text[j-1]相同，那么找到了一个公共元素，所以dp[i][j] = dp[i - 1][j - 1] + 1;
    b.如果text1[i - 1] 与 text2[j - 1]不相同
    那就看看text1[0, i - 2]与text2[0, j - 1]的最长公共子序列
    和 text1[0, i - 1]与text2[0, j - 2]的最长公共子序列，取最大的
    即: dp[i][j]= max(dp[i-1][j],dp[i][j-1])
3. 初始化为0
4. 确定遍历顺序

"""
#1.创建dp数组
text1 = "abcde"
text2 = "ace"
length1 = len(text1) + 1
length2 = len(text2) + 1
# 1.创建dp数组并初始化
dp = [[0 for _ in range(length1)] for _ in range(length2)]
for i in range(1, length2):
    for j in range(1, length1):
        if text1[j-1] == text2[i-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
print(dp[-1][-1])
