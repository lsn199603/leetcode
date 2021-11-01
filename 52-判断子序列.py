"""
给定字符串 s 和 t ，判断 s 是否为 t 的子序列。

字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。（例如，"ace"是"abcde"的一个子序列，而"aec"不是）。

1. 确定dp数组
dp[i][j]表示以下标i-1为结尾的字符串s,以下标j-1为结尾的字符串t,相同子序列的长度为dp[i][j]
2. 确定递推公式
if (s[i-1] == t[i-1])
    t中找到了一个字符s中也出现了
if (s[i-1] == t[i-1])
    相当于t要删除元素，继续匹配

"""
s = "abc"
t = "ahbgdc"
length_s = len(s)
length_t = len(t)
# 1. 创建dp数组及下标的含义 DP数组初始化
dp = [[0] * (length_t+1) for _ in range(length_s+1)]
print(dp)
# 2. 确定遍历顺序
for i in range(1, length_s+1):
    for j in range(1, length_t+1):
        if t[j-1] == s[i-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = dp[i][j-1]
if dp[-1][-1] == length_s:
    print(True)
else:
    print(False)


# 3. 递推公式
# 4. 推导dp数组