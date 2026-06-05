# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.tree1=[]
        self.tree2=[]
        def dfs(curr,t):
            if not curr:
                t.append(None)
                return 
            t.append(curr.val)
            dfs(curr.left,t)
            dfs(curr.right,t)
        dfs(p,self.tree1)
        dfs(q,self.tree2)

        return True if self.tree1 == self.tree2 else False
