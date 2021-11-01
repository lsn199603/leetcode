"""
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

 

示例 1：

输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
输出：6
解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。

单调栈
"""
height = [0,1,0,2,1,0,1,3,2,1,2,1]
ans = 0
stack = []
for i in range(len(height)):
    while (stack and height[stack[-1]] < height[i]):
        # 出栈
        temp = stack.pop()
        # 如果没有前一个元素，直接跳出
        if not stack:
            break
        # 左边元素的下标
        left = stack[-1]
        right = i
        width = right - left - 1
        length = min(height[left], height[right]) -height[temp]
        ans += width * length
    stack.append(i) # 下标入栈
print(ans)