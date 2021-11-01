"""
请根据每日 气温 列表 temperatures ，请计算在每一天需要等几天才会有更高的温度。如果气温在这之后都不会升高，请在该位置用 0 来代替。

示例 1:
输入: temperatures = [73,74,75,71,69,72,76,73]
输出: [1,1,4,2,1,1,0,0]
暴力解法：两层循环
优化解法：一层循环，以空间换时间，时间复杂度为0(n)
"""
temperatures = [30,40,50,60]
length = len(temperatures)
ans = [0] * length
stack = []
for i in range(length):
    temperature = temperatures[i]
    # 栈不为空，且放入元素大于栈顶元素
    while stack and temperature > temperatures[stack[-1]]:
        prev_index = stack.pop()
        ans[prev_index] = i - prev_index
    stack.append(i)
print(ans)

