"""
在两条独立的水平线上按给定的顺序写下 nums1 和 nums2 中的整数。

现在，可以绘制一些连接两个数字 nums1[i] 和 nums2[j] 的直线，这些直线需要同时满足满足：

 nums1[i] == nums2[j]
且绘制的直线不与任何其他连线（非水平线）相交。
请注意，连线即使在端点也不能相交：每个数字只能属于一条连线。
以这种方法绘制线条，并返回可以绘制的最大连线数。


示例 1：
输入：nums1 = [1,4,2], nums2 = [1,2,4]
输出：2
解释：可以画出两条不交叉的线，如上图所示。
但无法画出第三条不相交的直线，因为从 nums1[1]=4 到 nums2[2]=4 的直线将与从 nums1[2]=2 到 nums2[1]=2 的直线相交。
类似于47 最长公共子序列的问题

2. 确定递推公式
    a.text[i-1] 与 text[j-1]相同，那么找到了一个公共元素，所以dp[i][j] = dp[i - 1][j - 1] + 1;
    b.如果text1[i - 1] 与 text2[j - 1]不相同
    那就看看text1[0, i - 2]与text2[0, j - 1]的最长公共子序列
    和 text1[0, i - 2]与text2[0, j - 2]的最长公共子序列，取最大的
    即: dp[i][j]= max(dp[i-1][j],dp[i][j-1])
"""
nums1 = [1,4,2]
nums2 = [1,2,4]
len1 = len(nums1) + 1
len2 = len(nums2) + 1
# for i in range(len1):
#     for j in range(i)
# 1. 创建dp数组 dp[i][j]：长度为[0,i-1]的字符串text1与长度为[0,j-1]的字符串text2的最长公共子序列为dp[i][j]
dp = [[0 for _ in range(len1)] for _ in range(len2)]
# 2. 对动态数组表赋值
for i in range(1, len2):
    for j in range(1, len1):
        if nums1[j-1] == nums2[i-1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
print(dp[-1][-1])


