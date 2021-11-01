"""
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
输入：nums = [5,7,7,8,8,10], target = 8
输出：[3,4]
输入：nums = [5,7,7,8,8,10], target = 6
输出：[-1,-1]
"""
nums = [5,7,7,8,8,10]
target = 8
start  = -1
end = -1
n = len(nums)
if n == 1:
    if nums[0] == target:
        start, end = 0, 0
for i in range(n):
    if nums[i] == target:
        start = i
        for j in range(n-1, i-1, -1):
            if nums[j] == target:
                end = j
                break
        break
arr = []
arr.append(start)
arr.append(end)
print(arr)