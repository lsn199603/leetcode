"""
你这个学期必须选修 numCourses 门课程，记为 0 到 numCourses - 1 。

在选修某些课程之前需要一些先修课程。 先修课程按数组 prerequisites 给出，其中 prerequisites[i] = [ai, bi] ，表示如果要学习课程 ai 则 必须 先学习课程  bi 。

例如，先修课程对 [0, 1] 表示：想要学习课程 0 ，你需要先完成课程 1 。
请你判断是否可能完成所有课程的学习？如果可以，返回 true ；否则，返回 false 。
输入：numCourses = 2, prerequisites = [[1,0]]
输出：true
解释：总共有 2 门课程。学习课程 1 之前，你需要完成课程 0 。这是可能的。

课程安排图是否是有向无环图(DAG),但不能构成任何环路，否则课程前置条件将不成立。
拓扑排序，有向图（有向有环图，有向无环图）
1. list存储有向图的列表
2. 数组 存储每个节点的入度
3. deque 维持一个入度为0的节点的队列
    删除队列中的节点，直到队列中无元素
"""
import collections
numCourses = 2
prerequisites = [[1,0]]
# 存储有向图的列表
edges = collections.defaultdict(list)
# 存储每个节点的入度
indeg = [0] * numCourses
result = 0

# 字典值的填充和节点入度的统计
for info in prerequisites:
    edges[info[1]].append(info[0])
    indeg[info[0]] += 1
"""
collections.deque()
deque是双端队列（double-ended queue）的缩写，
由于两端都能编辑，deque既可以用来实现栈（stack）也可以用来实现队列（queue）。
添加一个元素append() appendleft()
添加一个元素extend() extendleft()
弹出一个元素pop()    popleft()
从尾部旋转到首步rotate(n)
从首步旋转到尾部rotate(-n)
计算队列元素数count()
"""
# 将入度为0的节点添加到队列
q = collections.deque([u for u in range(numCourses) if indeg[u] == 0])
# 循环知道队列中无节点 先进先出，popleft()
while q:
    # 队列删除入度为0的节点
    u = q.popleft()
    # 计算删除的节点数
    result += 1
    # 将以u为先修课程的节点的入读都减1 如果节点入度为0则添加到队列
    for v in edges[u]:
        indeg[v] -= 1
        if indeg[v] == 0:
            q.append(v)
print(result)