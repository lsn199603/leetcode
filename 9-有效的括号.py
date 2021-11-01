"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。
ss
有效字符串需满足：
左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
输入：s = "()[]{}"
输出：true
栈的方法
"""
s = "({[{}})"
stack = []
for c in s:
    if c == "(" or c == "{" or c == "[":
        stack.append(c)
    else:
        if not stack:
            print(False)
        if c == ')':
            temp = stack.pop()
            if temp != '(':
                print(False)
        elif c == ']':
            temp = stack.pop()
            if temp != '[':
                print(False)
        elif c == '}':
            temp = stack.pop()
            if temp != '{':
                print(False)
print(stack == [])