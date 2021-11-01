"""
以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。请你合并所有重叠的区间，并返回一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间。

 
输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
输出：[[1,6],[8,10],[15,18]]
解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].

解题思路如下：

先对输入数组按照区间左边的值进行升序排列
初始化一个变量 outputs，用于存储合并直接的区间结果
遍历排序后的所有区间，针对每个区间做如下的处理：
如果当前处理的区间是第一个区间的话，那么直接将区间加入到 outputs
比较当前处理区间左边的值 (currLeft) 和 outputs 中最后一个区间右边的值 (outputsLastRight) ：
如果 outputsLastRight < currLeft，说明没有重叠，那么直接将当前处理的区间加入到 outputs
否则，说明有重叠，那么将 outputs 中最后一个区间的右边的值更新为：当前处理区间右边值和 outputsLastRight 的最大值
将 outputs 转成数组，并返回


"""
intervals = [[2,6],[1,3],[8,10],[15,18]]

if not intervals:
    print(intervals)
intervals.sort(key=lambda x: x[0])
result = []
result.append(intervals[0])
for i in range(1, len(intervals)):
    last = result[-1]
    if last[1] >= intervals[i][0]:
        result[-1] = [last[0], max(last[1], intervals[i][1])]
    else:
        result.append(intervals[i])
print(result)
