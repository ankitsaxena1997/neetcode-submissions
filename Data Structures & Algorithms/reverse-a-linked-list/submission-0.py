# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head==None:
            return head
            
        temp=ListNode()
        temp.next= None
        temp.val = head.val

        while head.next:

            temp1 = ListNode()
            temp1.val = head.next.val
            temp1.next = temp
            temp = temp1

            head = head.next
        
        return temp



        