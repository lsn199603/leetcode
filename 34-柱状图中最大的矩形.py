"""
给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。

求在该柱状图中，能够勾勒出来的矩形的最大面积。
输入：heights = [2,1,5,6,2,3]
输出：10
解释：最大的矩形为图中红色区域，面积为 10

固定高，找最大的宽
"""
heights = [2,1,5,6,2,3]
length = len(heights)
if length  == 0:
    print(0)
if length == 1:
    print(heights[0])
# 空间换时间 存储
left_i = [0] * length
right_i = [0] * length
# 哨兵
left_i[0] = -1
right_i[-1] = length
# 单调找
# 左边的每个存储对应位置的左边界
mono_stack = list()
for i in range(length):
    while mono_stack and heights[mono_stack[-1]] > heights[i]:
        mono_stack.pop()
    left_i[i] = mono_stack[-1] if mono_stack else  -1
    mono_stack.append(i)
# 右边的每个存储对应位置的右边界
print(left_i)
mono_stack = list()
for i in range(length-1, -1, -1):
    while mono_stack and heights[mono_stack[-1]] > heights[i]:
        mono_stack.pop()
    right_i[i] = mono_stack[-1] if mono_stack else  length
    mono_stack.append(i)
print(right_i)
ans = max((right_i[i] - left_i[i] - 1) * heights[i] for i in range(length))
print(ans)