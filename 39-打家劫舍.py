"""
你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。
输入：[1,2,3,1]
输出：4
解释：偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
     偷窃到的最高金额 = 1 + 3 = 4 。
动态规划：
1. 定义子问题
2. 写出子问题的递推关系
S_n = max(S_n-1,S_n-2+H_n)
3. 确定DP数组的计算顺序
4. 空间优化
"""
nums = [1,1,1,2]
if len(nums) == 0:
    print(0)
elif len(nums) == 1:
    print(nums[0])
elif len(nums) == 2:
    print(max(nums))
dp = [0 for _ in range(len(nums))]
dp[0] = nums[0]
dp[1] = max(nums[0], nums[1])
for i in range(2, len(nums)):
    dp[i] = max(dp[i-1], dp[i-2]+nums[i])
print(dp[len(nums) - 1])