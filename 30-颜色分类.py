"""
给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

输入：nums = [2,0,2,1,1,0]
输出：[0,0,1,1,2,2]

快速排序 partition
循环不变量
"""
# all in [0, zero) = 0
# all in [zero, i) = 1
# all in [two, len - 1] = 2

nums = [2,0,2,1,1,0]
nums.sort()
print(nums)
def swap(nums, index1, index2):
    nums[index1], nums[index2] = nums[index2], nums[index1]

size = len(nums)
if size < 2:
    print(nums)
zero = 0
two = size
i = 0
while i < two:
    if nums[i] == 0:
        swap(nums, i, zero)
        i += 1
        zero += 1
    elif nums[i] == 1:
        i += 1
    else:
        two -= 1
        swap(nums, i, two)