"""
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
输入：digits = "23"
输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]
"""
digits = "23"
if not digits:
    print([])
Dict = {'2': {'a', 'b', 'c'},
        '3': {'d', 'e', 'f'}, '4': {'g', 'h', 'i'}, '5': {'j', 'k', 'l'},
        '6': {'m', 'n', 'o'}, '7': {'p', 'q', 'r', 's'}, '8': {'t', 'u', 'v'},
        '9': {'w', 'x', 'y', 'z'}}
length = len(digits)
res = []
def dfs(tmp ,index):
    if index == length:
        res.append(tmp)
        return
    for c in Dict[digits[index]]:
        print(c)
        print(tmp+c, index+1)
        dfs(tmp+c, index+1)

dfs('', 0)
print(res)