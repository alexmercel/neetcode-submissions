# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node,depth):
            if not node:
                return depth
            depthl=dfs(node.left,depth+1)
            depthr=dfs(node.right,depth+1)
            return max(depthl,depthr)
        return dfs(root,0)
        