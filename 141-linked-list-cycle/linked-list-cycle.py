# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head
        if head is None:
            return False

        if fast.next is None:
            return False
        
        while fast and fast.next:
           
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        return False

        # slow = head
        # while slow != fast and fast.next:
        #     slow = slow.next
        #     fast = fast.next

        # return slow == fast
        