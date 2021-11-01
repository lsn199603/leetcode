"""
给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。
子序列是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。

输入：nums = [10,9,2,5,3,7,101,18]
输出：4
解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。

"""
nums = [10,9,2,5,3,7,101,18]
length = len(nums)
if length <= 1:
    print(length)
# 1. 创建dp数组 dp[i]表示i之前包括i的最长上升子序列的长度
# 每个数字的最长子序列为1
dp = [1] * length
# 存最大值
result = 0
#3. 先下后上，先左后右
for i in range(1, length):
    for j in range(i):
        if nums[i] > nums[j]:
            # 要取dp[j] + 1的最大值。
            dp[i] = max(dp[i],dp[j]+1)
    result = max(result, dp[i])#取长的子序列
print(result)

