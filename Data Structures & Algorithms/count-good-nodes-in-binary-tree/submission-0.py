# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res=0
        def dfs(node,highest):
            nonlocal res
            if not node:
                return
            if node.val >= highest:
                res+=1
            if node.left:
                dfs(node.left,max(highest,node.val))
            if node.right:
                dfs(node.right,max(highest,node.val))
        dfs(root,float("-inf"))
        return res