"""
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。

注意：答案中不可以包含重复的三元组。

输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]
"""
nums = [-1,0,1,2,-1,-4]
n = len(nums)
res = []
if (not nums or n < 3):
    print([])
# 对数组进行排序
nums.sort()
for i in range(n):
    if nums[i] > 0:
        print(res)
    if (i > 0 and nums[i] == nums[i-1]):
        continue
    L = i + 1
    R = n - 1
    while(L < R):
        if nums[L] + nums[i] + nums[R] > 0:
            R -= 1
        elif nums[L] + nums[i] + nums[R] < 0:
            L += 1
        elif nums[L] + nums[i] + nums[R] == 0:
            res.append([nums[i],nums[L],nums[R]])
            # 执行循环，判断左界和右界是否和下一位置重复，去除重复解
            while(L < R and nums[L] == nums[L+1]):
                L += 1
            while (L < R and nums[R] == nums[R - 1]):
                R -= 1
            # 并同时将 L,R 移到下一位置，寻找新的解
            L = L + 1
            R = R - 1
print(res)