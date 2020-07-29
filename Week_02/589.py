class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        '''res = []
        def help(root):
            if root is None:
                return None
            help(root.left)
            res.append(root.val)
            help(root.right)
        help(root)
        return res'''
        if root is None:
            return []
        stack = []
        res = []
        cur = root
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            temp = stack.pop()
            res.append(temp.val)
            cur = temp.right
        return res