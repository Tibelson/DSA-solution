# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        # prev = None
        while curr and curr.next:
            # prev = curr
            # curr = curr.next
            
            if curr.val == curr.next.val:
                curr.next = curr.next.next

            else:
                curr = curr.next
        
        
        # while curr:
            
        #     if curr.val == prev.val:
        #         return curr
            

        return head
                

        