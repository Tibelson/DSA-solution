# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = head
        fast = head
        while fast and fast.next:
            fast=fast.next.next
            slow = slow.next

        # print(slow.val)
        curr = slow.next
        prev = None
        slow.next = None
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        # print(head)
        h1 = head
        h2 = prev
        while h2:
            link1 = h1.next
            link2 = h2.next
            h1.next = h2
            h2.next = link1
            h1, h2  = link1, link2


        # tail = head
        # while tail.next is not None:
        #     tail = tail.next

        # # print(tail.val)
        
        # curr = head
        # slow = tail
        # while curr and curr.next and slow:
        #     next_node = curr.next
        #     curr.next = tail
        #     curr = tail
        #     curr = next_node
        #     slow.next = curr
            # tail.next = next_node
            # next_node = next_node.next

            # tail.next = curr.next
            # curr.next = curr.next.next

