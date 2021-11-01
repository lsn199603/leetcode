"""
给你一个链表数组，每个链表都已经按升序排列。

请你将所有链表合并到一个升序链表中，返回合并后的链表。
输入：lists = [[1,4,5],[1,3,4],[2,6]]
输出：[1,1,2,3,4,4,5,6]
比较直观的做法，直接利用分治的方法，接下来的重点就是如何设计好递归函数的参数了。
递归函数的参数还是借用二分的写法，采用左右边界来确定链表的个数。
也可以通过建立一个堆来合并这k个链表。
分治
"""
from Cython.Compiler.ExprNodes import ListNode


class Solution:
    def mergeKLists(self, lists: list[ListNode]) -> ListNode:
        if not lists:
            return
        n = len(lists)
        return self.merge(lists, 0, n - 1)


    def merge(self, lists, left, right):
        """
        :param lists:  链表数组
        :param left: 左指针
        :param right: 右指针
        :return:
        """
        if left == right:
            return lists[left]
        # 寻找数组中的中间链表
        mid = left + (right - left) // 2
        l1 = self.merge(lists, left, mid)
        l2 = self.merge(lists, mid + 1, right)
        return self.mergeTwoLists(l1, l2)

    def mergeTwoLists(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

