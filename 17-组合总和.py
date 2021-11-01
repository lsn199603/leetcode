"""
给定一个无重复元素的正整数数组 candidates 和一个正整数 target ，找出 candidates 中所有可以使数字和为目标数 target 的唯一组合。

candidates 中的数字可以无限制重复被选取。如果至少一个所选数字数量不同，则两种组合是唯一的。 

对于给定的输入，保证和为 target 的唯一组合数少于 150 个。

输入: candidates = [2,3,6,7], target = 7
输出: [[7],[2,2,3]]
DFS
"""
candidates = [2, 3, 6, 7]
target = 7


def dfs(candidates, begin, size, path, res, target):
    """
    :param candidates: 输出数组
    :param begin: 开始
    :param size: 输入数组长度
    :param path: 路径
    :param res:
    :param target: 目标值
    :return:
    """
    # 减到0或者负数的时候停止
    if target < 0:
        return
    if target == 0:
        res.append(path)
        return

    for index in range(begin, size):
        print("递归之前")
        print(path)
        dfs(candidates, index, size, path + [candidates[index]], res, target - candidates[index])
        print("递归之后")
        print(path)

size = len(candidates)
if size == 0:
    print([])
path = []
res = []
dfs(candidates, 0, size, path, res, target)
print(res)