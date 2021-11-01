"""
给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。
请你将两个数相加，并以相同形式返回一个表示和的链表。
你可以假设除了数字 0 之外，这两个数都不会以 0 开头。
输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[7,0,8]
解释：342 + 465 = 807.
"""

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from Cython.Compiler.ExprNodes import ListNode


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 进位 两数相加
        carry = 0
        head = point = ListNode(0)

        while l1 or l2:
            new_point = ListNode(0)
            # 判断l1是否达到尾端
            if not l1:
                sum_ = l2.val + carry
                new_point.val = sum_ % 10
                carry = sum_ // 10
                l2 = l2.next
            # 判断l2是否达到尾端
            elif not l2:
                sum_ = l1.val + carry
                new_point.val = sum_ % 10
                carry = sum_ // 10
                l1 = l1.next
            else:
                sum_ = (l1.val + l2.val +carry)

                new_point.val = sum_ % 10
                carry = sum_ // 10

                l1 = l1.next
                l2 = l2.next
            point.next = new_point
            point = point.next
        if carry:
            new_point = ListNode(1)
            point.next = new_point
        return head.next



