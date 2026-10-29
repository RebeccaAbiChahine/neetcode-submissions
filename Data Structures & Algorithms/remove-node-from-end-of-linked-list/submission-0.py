# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # we want to go to the end of the linkedlist and remove the nth element from there
        #we can use a stack to store the elements of the linkedlist, then loop from the last index until n-> find the element at n, then we go through our linkedlist ... when we find curr.val = element at n -> remove it by doing curr.val = curr.next.next
        first = head
        second = head
        secondStartingPoint = n


        while secondStartingPoint > 0:
            second = second.next
            secondStartingPoint -=1

        if not second: 
            return head.next
        
        prev = first
        while second:
            prev = first
            first = first.next
            second = second.next
        prev.next = first.next
        return head