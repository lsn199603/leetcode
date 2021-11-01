"""
“下一个排列”的定义是：给定数字序列的字典序中下一个更大的排列。如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。

我们可以将该问题形式化地描述为：给定若干个数字，将其组合为一个整数。如何将这些数字重新排列，以得到下一个更大的整数。如 123 下一个更大的数为 132。如果没有更大的整数，则输出最小的整数。
输入：nums = [1,2,3]
输出：[1,3,2]

"""
nums = [1,2,3]
# 定义一个将nums中[i,j]区间元素原地倒排的函数
def reverse(nums, i, j):
    while(i < j):
        i += 1
        j -= 1
n = len(nums)
firstIndex = -1
# 从右至左找到第一个相邻降序对
for i in range(n-1, -1, -1):
    if nums[i] > nums[i-1]:
        firstIndex = i-1
        break
# 若果从右至左没有找到降序对，则数组是降序排序的，即本身是最大的，所以反转数组，使之成为最小的排列
if firstIndex == -1:
    nums.reverse()
print(nums)
# 从右至左找第一个大于nums[firstIndex]的大数
secondeIndex=-1
for i in range(n-1, firstIndex, -1):
    if nums[i] > nums[firstIndex]:
        secondeIndex = i
        break
nums[firstIndex], nums[secondeIndex] = nums[secondeIndex], nums[firstIndex]
reverse(nums, firstIndex+1, n-1)
print(nums)
