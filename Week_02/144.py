class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None:
            return []
        stack = [root]
        res = []
        while stack:
            res.append([temp.val for temp in stack])
            stack = [temp for item in stack for temp in item.children]
        return res