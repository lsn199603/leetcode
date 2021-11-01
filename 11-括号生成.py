"""
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

有效括号组合需满足：左括号必须以正确的顺序闭合。
输入：n = 3
输出：["((()))","(()())","(())()","()(())","()()()"]
回溯+剪枝
1. 当前左右括号都有大于 00 个可以使用的时候，才产生分支；
2. 产生左分支的时候，只看当前是否还有左括号可以使用；
3. 产生右分支的时候，还受到左分支的限制，右边剩余可以使用的括号数量一定得在严格大于左边剩余的数量的时候，才可以产生分支；
4. 在左边和右边剩余的括号数都等于 00 的时候结算。
"""
n = 3
res = []
cur_str = ''
def dfs(cur_str, left, right):
    """
    :param cur_str: 从根结点到叶子结点的路径字符串
    :param left: 左括号还可以使用的个数
    :param right: 右括号还可以使用的个数
    :return:
    """
    # 定义递归函数的结束条件
    if left == 0 and right == 0:
        res.append(cur_str)
        return
    # 左括号数量严格大于右括号的数量时剪枝
    if left > right:
        return
    if left > 0:
        dfs(cur_str + '(', left-1, right)
    if right > 0:
        dfs(cur_str + ')', left, right-1)


dfs('', n, n)
print(res)