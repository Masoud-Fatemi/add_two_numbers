# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        first, second = "", ""
        result = cur = ListNode()

        while True:
            first = str(l1.val) + first
            if l1.next == None:
                break
            l1 = l1.next

        while True:
            second = str(l2.val) + second
            if l2.next == None:
                break
            l2 = l2.next

        sum = int(first) + int(second)
        sum = list(str(sum))
    
        for digit in reversed(sum):
            cur.next = ListNode(digit)
            cur = cur.next
            
        return result.next