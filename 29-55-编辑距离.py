"""
给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数 。

你可以对一个单词进行如下三种操作：

插入一个字符
删除一个字符
替换一个字符

输入：word1 = "horse", word2 = "ros"
输出：3
解释：
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')

1. 确定dp数组以及下标的含义
dp[i][j]表示以下标i-1结尾的字符串word1，和以下标j-1为结尾的字符串word1,最近编辑距离为dp[i][j]
2.确定递推公式
if (word1[i-1] == word2[j-1])
    不操作 dp[i][j] = dp[i-1][j-1]
if (word1[i-1] != word2[j-1])
    增
    删   dp[i][j] = dp[i-1][j] + 1 dp[i][j] = dp[i][j-1] + 1
    换   dp[i][j] = adp[i-1][j-1] + 1
3. dp数组初始化
    dp[i][0] = i 和 dp[0][j] = j
4. 确定遍历顺序
    从左到右，从上到下去遍历
5. 举例推导dp数组

"""
word1 = "horse"
word2 = "ros"
n = len(word1) + 1
m = len(word2) + 1
# 1. 创建dp数组
dp = [[0] * n for _ in range(m)]
# 2. 初始化dp数组
for i in range(m):
    dp[i][0] = i
for j in range(n):
    dp[0][j] = j
# 3. 递推公式对dp数组赋值
for i in range(1, m):
    for j in range(1, n):
        if word1[j-1] == word2[i-1]:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = min(dp[i - 1][j - 1]+1,dp[i][j-1]+1,dp[i-1][j]+1)
print(dp[-1][-1])



# if n * m == 0:
#     print(n + m)
# # DP 数组
# dp = [[0] * (m + 1) for _ in range(n + 1)]
# # 边界状态初始化
# for i in range(n + 1):
#     dp[i][0] = i
# for j in range(m + 1):
#     dp[0][j] = j
# print(dp)
# # 计算所有 DP 值
# for i in range(1, n + 1):
#     for j in range(1, m + 1):
#         left = dp[i - 1][j] + 1
#         down = dp[i][j - 1] + 1
#         left_down = dp[i - 1][j - 1]
#         if word1[i - 1] != word2[j - 1]:
#             left_down += 1
#         dp[i][j] = min(left, down, left_down)
#
# print(dp[n][m])

