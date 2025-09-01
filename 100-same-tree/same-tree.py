# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
       
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
      
        # left_p = self.isSameTree(p.left,q.left)
        # mid_p =[p.val]
        # right_p = self.isSameTree(p.right,q.right)

        # if not q:
        #     return []

        # left_q = self.isSameTree(q.left)
        # mid_q = [q.val]
        # right_q = self.isSameTree(q.right)


        # return (left_p + mid_p + right_p) == (left_q + mid_q + right_q)


        