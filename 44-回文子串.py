"""
给你一个字符串 s ，请你统计并返回这个字符串中 回文子串 的数目。

回文字符串 是正着读和倒过来读一样的字符串。

子字符串 是字符串中的由连续字符组成的一个序列。

具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被视作不同的子串。

输入：s = "abc"
输出：3
解释：三个回文子串: "a", "b", "c"
"""
s = "abc"
length = len(s)
# 1. 创建DP数组 及 初始化
dp = [[False] * length for _ in range(length)]
# 回文子串的数量
res = 0
"""
递推公式：
1. s[i] != s[j] 不是回文子串
2. s[i] == s[j] 
   a. i = j 同一个字符串 是回文子串
   b. i - j <= 1

"""
for i in range(length-1, -1, -1):
    for j in range(i, length):
        if s[i] == s[j]:
            if j - i <= 1:
                res += 1
                dp[i][j] = True
            elif dp[i+1][j-1]:
                res += 1
                dp[i][j] = True
print(dp)