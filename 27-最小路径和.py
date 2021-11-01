"""
给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
说明：每次只能向下或者向右移动一步。
输入：grid = [[1,3,1],[1,5,1],[4,2,1]]
输出：7
解释：因为路径 1→3→1→1→1 的总和最小
四种情况：
1. i=0, j=0 dp[i][j] = grid[i][j]
2. i=0, j!=0 dp[i][j]  = grid[i][j] + dp[i][j-1]
3. i!=0, j=0 dp[i][j] = grid[i][j] + dp[i-1][j]
3. i!=0, j!=0 dp[i][j] = min(grid[i][j-1], dp[i-1][j]) + grid[i][j]
"""
grid = [[1,3,1],[1,5,1],[4,2,1]]
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if i==0 and j ==0 :
            continue
        elif i==0 and j !=0:
            grid[i][j] = grid[i][j - 1] + grid[i][j]
        elif i!=0 and j ==0:
            grid[i][j] = grid[i-1][j] + grid[i][j]
        else:
            grid[i][j] = min(grid[i][j - 1], grid[i-1][j]) + grid[i][j]
print(grid[-1][-1])