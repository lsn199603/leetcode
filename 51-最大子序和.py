"""
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
输出：6
解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。
"""
# 1.创建dp数组
nums = [-100000]
length = len(nums)
dp = [0] * length
dp[0] = nums[0]
res = 0
for i in range(1, length):
    dp[i] = max(dp[i-1] + nums[i],nums[i])
print(max(dp))
