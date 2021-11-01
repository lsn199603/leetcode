"""
给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
输出：true

"""
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
length = len(board)
width = len(board[0])
flags  = [[0] * width for _ in  range(length)]
res = 0
def dfs(x, y, count, res):
    """
    :param x:
    :param y:
    :param count:
    :param res:
    :return:
    """

    # 判断终止条件
    if count == len(word):
        res = 1
        return res
    for delta_x, delta_y in [(1,0), (-1, 0), (0, 1), (0, -1)]:
        if res == 1:
            return res
        if x + delta_x >=0 and x + delta_x <= length - 1 and y + delta_y >= 0 and y + delta_y <= width - 1 and flags[x + delta_x][y + delta_y] == 0 and board[x+delta_x][y+delta_y] == word[count]:
            flags[x + delta_x][y + delta_y] = 1
            dfs(x + delta_x, y + delta_y, count + 1,  res)
            flags[x + delta_x][y + delta_y] = 0

for i in range(length):
    for j in range(width):
        if board[i][j] == word[0]:
            flags[i][j] = 1
            res = dfs(i, j, 1, res)
            flags[i][j] = 0
            if res == 1:
                print(True)
print(False)