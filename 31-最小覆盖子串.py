"""
给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。

 

注意：

对于 t 中重复字符，我们寻找的子字符串中该字符数量必须不少于 t 中该字符数量。
如果 s 中存在这样的子串，我们保证它是唯一的答案。
输入：s = "ADOBECODEBANC", t = "ABC"
输出："BANC"

子串：强调连续性
滑动窗口题目。需要维护两个字典，和两个指针。
字符频数数组
引入distance
"""
import collections
s = "ADOBECODEBANC"
t = "ABC"
need = collections.defaultdict(int)
for c in t:
    need[c] += 1
needCnt = len(t)
# 记录起始位置
i = 0
#用两个元素，方便之后记录起终点
# float('inf') : 正无穷
res = (0, float('inf'))
# 1， 增加右边界使窗口包含t
for j, c in enumerate(s):
    # 判断字符是否包含在t中 ,如果包含则总数减1
    if need[c] > 0:
        needCnt -= 1
    # 把t中的元素加到字典里，不包含在s中的元素值为负数
    need[c] -= 1
    print(need)
    print(needCnt)
    # 2. 找到包含t的字符串，再收缩左边界直到无法再去掉元素   !注意，处理的是i
    if needCnt == 0:
        # 收缩左边界，i左边界的下标 i = 0
        while True:
            c = s[i]
            # need[c]==0 表示再去掉这个元素就不能包含t子串了
            if need[c] == 0:
                break
            else:
                # 之前不是t中的元素减1，
                need[c] += 1
                # 移到下一个坐标
                i += 1
        # 赋值res为最小子串
        if j - i < res[1] - res[0]:
            res = (i, j)
    # 3. i多增加一个位置，准备开始下一次循环(注意这步是在 needCnt == 0里面进行的 )
        need[s[i]] += 1
        needCnt += 1  # 由于 移动前i这个位置 一定是所需的字母，因此NeedCnt才需要+1
        i += 1
print('' if res[1]>len(s) else s[res[0]:res[1]+1])
