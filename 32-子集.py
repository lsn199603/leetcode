"""
给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。

解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。
输入：nums = [1,2,3]
输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
深度优先遍历
回朔算法

"""
nums = [1,2,3]
res = []
length = len(nums)
if length == 0:
    print(nums)
# def dfs(i, temp):
#     res.append(temp)
#     for j in range(i, length):
#         dfs(j+1, temp + [nums[j]])
# dfs(0,[])
# print(res)
# 深度优先遍历
def dfs(nums, len, index, path, res):

    """
    :param nums:  输入数组
    :param len: 数组的长度
    :param index: 起始下标
    :param path:
    :param res:
    :return:
    """
    if index == len:
        res.append(path)
        return
    # 是否考虑这个元素
    for i in range(2):
        # 考虑这层元素
        if i == 1:
            dfs(nums, len, index+1, path + [nums[index]], res)
        # 不考虑考虑这层元素
        else:
            dfs(nums, len, index + 1, path, res)


dfs(nums, length, 0, [], res)
print(res)