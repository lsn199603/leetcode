"""
给你一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号子串的长度。
输入：s = "(()"
输出：2
解释：最长有效括号子串是 "()"
"""
s = "((()))"
if not s:
    print(0)
stack = [-1]
res = 0
for i in range(len(s)):
    if s[i] == "(":
        stack.append(i)
    else:
        stack.pop()
        if not stack:
            stack.append(i)
        else:
            res = max(res, i - stack[-1])

print(res)


