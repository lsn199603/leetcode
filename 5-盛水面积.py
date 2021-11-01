"""
给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0) 。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器。
输入：height = [4,3,2,1,4]
输出：16
简单的DP:
res = max{min(a[i], a[j])*(j - i)}
采用双指针进行搜索，将a[i]和a[j]中较小的坐标进行移动，因为将较大的往里进行移动，最终的结果一定会变小。
左右两头:双指针
"""
height = [4,3,2,1,4]
l, r = 0, len(height) - 1
ans = 0
while l < r:
    area = min(height[l], height[r]) * (r - l)
    ans = max(ans, area)
    if height[l] <= height[r]:
        l += 1
    else:
        r -= 1

print(ans)