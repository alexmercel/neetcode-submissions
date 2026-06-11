class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True
        def dfs(curr):
            if not curr:
                return 0
                
            right_h = dfs(curr.right)
            left_h = dfs(curr.left)

            if abs(right_h - left_h) > 1:
                self.balanced = False

            return 1 + max(right_h, left_h)
        dfs(root)
        return self.balanced