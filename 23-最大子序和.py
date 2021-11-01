"""
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
输出：6
解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。

题目只要求返回结果，不要求得到最大的连续子数组是哪一个。这样的问题通常可以使用「动态规划」解决。
为了保证计算子问题能够按照顺序、不重复地进行，动态规划要求已经求解的子问题不受后续阶段的影响。这个条件也被叫做「无后效性」。换言之，动态规划对状态空间的遍历构成一张有向无环图，遍历就是该有向无环图的一个拓扑序。有向无环图中的节点对应问题中的「状态」，图中的边则对应状态之间的「转移」，转移的选取就是动态规划中的「决策」。


"""
# 若前一个元素大于0，则将其加到当前元素上
nums = [-2,1,-3,4,-1,2,1,-5,4]
length = len(nums)
# 简单的动态规划
# for i in range(1, len(nums)):
#     if nums[i-1] > 0:
#         nums[i] += nums[i-1]
# print(max(nums))
# 复杂的动态规划
# 创建一个动态规划表
dp = [0] * length
dp[0] = nums[0]
res = nums[0]
for i in range(1, length):
    if dp[i-1] < 0:
        dp[i] = nums[i]
    else:
        dp[i] = dp[i-1] + nums[i]
    res = max(res,dp[i])
print(res)