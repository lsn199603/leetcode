"""
给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。
输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
DFS

"""
def dfs(nums, length, depth, path, used, res):
    """
     状态：每一个结点表示求解问题的不同阶段
    深度优先遍历在回到上一层结点需"状态重置"
    状态变量
    :param nums: 输入数组
    :param length: 数组的长度
    :param depth: 递归到第几层，判断是否选完了所有数
    :param path:   已经选择的数 栈
    :param used:  布尔数组 used 选择过的数
    :param res:
    :return:
    """
    # 递归终止的条件 深度等于数组得长度
    if (depth == length):
        # 深拷贝和浅拷贝
        res.append(path[:])
        return
    for i in range(length):
        if used[i]:
            continue
        path.append(nums[i])
        used[i] = True
        dfs(nums, length, depth+1, path, used, res)
        path.pop()
        used[i] = False













# def dfs(nums, length, depth, path, used, res):
#     """
#     :param nums:  输出数组
#     :param length: 输入数组的长度
#     :param depth: 深度
#     :param path: 排列结果
#     :param used: 使用过的数
#     :param res: 最后的结果
#     :return:
#     """
#     # 到0层的时候停止
#     if depth == length:
#         # path1= path.copy()
#         # print(path[:])
#         res.append(path[:])
#         return
#     # 循环树的横向
#     for i in range(length):
#         if (used[i]):
#             continue
#         path.append(nums[i])
#         used[i] = True
#         dfs(nums, length, depth+1, path, used, res)
#         path.pop()
#         used[i] = False

# nums = [1,2,3]
# length = len(nums)
# if length == 0:
#     print([])
# path = []
# res = []
# used = [False for _ in range(length)]
# dfs(nums, length, 0, path, used, res)
# print(res)


# 判断是否是回文字符串
def funa(a):
    print(a)
    length = len(a)
    flag = "False"
    for i in  range(length):
        b = str(a[i])
        c = b[::-1]
        if c == b:
            flag = "NO"
        else:
            flag =  "YES"
    return flag
def funb(nums, length, depth, used, path, res):
    """
    :param nums:
    :param length:
    :param depth:
    :param used:
    :param path:
    :param res:
    :return:
    """
    # 递归的终止条件
    if depth == length:
        res.append(path[:])
        return
    for i in range(length):
        if used[i]:
            continue
        path.append(nums[i])
        used[i] = True
        funb(nums, length, depth+1, used, path, res)
        used[i] = False
        path.pop()
    return res
n = eval(input())

for i in range(n):
    a = input()
    length = len(a)
    if length == 1:
        print("NO")
    else:
        used = [False for _ in range(length)]
        path = []
        res = []
        nums = list(a)
        re = funb(nums, length, 0, used, path, res)
        print(re)
        flag = funa(re)
        print(flag)
# nums = "abccba"
# nums = list(nums)
# print(nums)
# length = len(nums)
# used = [False for _ in range(length)]
# path = []
# res = []
# re = funb(nums, length, 0, used, path, res)
# print(re)