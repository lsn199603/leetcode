"""
给定一个非负整数数组 nums ，你最初位于数组的 第一个下标 。
数组中的每个元素代表你在该位置可以跳跃的最大长度。
判断你是否能够到达最后一个下标。
输入：nums = [2,3,1,1,4]
输出：true

"""
nums = [3,2,1,0,4]
length = len(nums)
# 当前位置能够走到的最远距离
k = 0
for i in range(length):
    if i > k:
        print(False)
    k = max(k, i+nums[i])
print(True)