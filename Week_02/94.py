class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        '''res = []
        def help(root):
            if root is None:
                return []
            res.append(root.val)
            help(root.left)
            help(root.right)
        help(root)
        return res'''
        if root is None:
            return []
        stack = [root]
        res = []
        while stack:
            temp = stack.pop()
            res.append(temp.val)
            if temp.right:
                stack.append(temp.right)
            if temp.left:
                stack.append(temp.left)
        return res