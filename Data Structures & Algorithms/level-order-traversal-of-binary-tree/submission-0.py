# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        small_res = res = []
        q = deque([(1,root)])
        curr_lvl = 0
        while q:
            lvl, curr = q.popleft()
            if lvl > curr_lvl:
                if small_res:
                    res.append(small_res)
                small_res = [curr.val]
            else:
                small_res.append(curr.val)
            curr_lvl = lvl
            if curr.left:
                q.append((lvl +1,curr.left))
            if curr.right:
                q.append((lvl+1,curr.right))
        if small_res:
            res.append(small_res)
        return res
            

        