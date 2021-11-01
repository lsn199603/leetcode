"""
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
输入：l1 = [1,2,4], l2 = [1,3,4]
输出：[1,1,2,3,4,4]
"""
from Cython.Compiler.ExprNodes import ListNode


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val <= l2.val:
            """
            print(l1.next)
            ListNode{val: 2, next: ListNode{val: 4, next: None}}
            ListNode{val: 4, next: None}
            None
            """
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            """
            print(l1)
            print(l2.next)
            ListNode{val: 2, next: ListNode{val: 4, next: None}}
            ListNode{val: 3, next: ListNode{val: 4, next: None}}
            ListNode{val: 4, next: None}
            ListNode{val: 4, next: None}
            """
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
