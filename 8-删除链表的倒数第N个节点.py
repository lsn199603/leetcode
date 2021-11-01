"""

给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
进阶：你能尝试使用一趟扫描实现吗？

输入：head = [1,2,3,4,5], n = 2
输出：[1,2,3,5]
快慢指针，基本操作，需要注意的是有一种情况是直接删除头节点。
1. 我们先让快指针fast向前移动n+1步。
2. 让慢指针slow和快指针fast同时向前移动，每次移动一步，直到快指针fast指向null。
"""
from Cython.Compiler.ExprNodes import ListNode


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head:
            return None
        # 虚拟节点
        temp = head
        # 用来计算链表长度
        count = 0
        """
        temp
        ListNode{val: 1, next: ListNode{val: 2, next: ListNode{val: 3, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}}}
        ListNode{val: 2, next: ListNode{val: 3, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}}
        """
        while (temp):
            count += 1
            if count == n:
                break
            temp = temp.next

        slow = head
        fast = temp

        # pre慢指针的前一个指针
        pre = None
        # 快指针和慢指针通向前走,直到快指针fast指向null。
        while (fast.next):
            fast = fast.next
            pre = slow
            slow = slow.next
        if not pre:
            return head.next
        pre.next = slow.next
        """
        print(pre)
        print(slow)
        print(head)
        ListNode{val: 3, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}
        ListNode{val: 4, next: ListNode{val: 5, next: None}}
        ListNode{val: 1, next: ListNode{val: 2, next: ListNode{val: 3, next: ListNode{val: 5, next: None}}}}

        """
        return head