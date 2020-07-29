
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        queue = [root]
        list = []
        while queue:
             temp = queue.pop()
             list.append(temp.val)
             for i in temp.children:
                 queue.append(i)
        return list[::-1]