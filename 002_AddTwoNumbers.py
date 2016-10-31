# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num = self.sum_num(l1)+self.sum_num(l2)
        str_num = str(num)[::-1]
        node = ListNode(str_num[0])
        temp = node
        for x in str_num[1::]:
            temp.next = ListNode(x)
            temp = temp.next
        return node
        
    def sum_num(self,l):
        m,n = 0,0
        while l:
            m,l = m+l.val*10**n,l.next
            n = n+1
        return m