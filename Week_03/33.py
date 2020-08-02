class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    #搜索二维矩阵
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        m = len(matrix)
        n = len(matrix[0])
        left,right = 0,m*n
        while left < right:#一定要这样搭配，要不然会出错
            mid = (left + right)//2
            i = mid//n
            j = mid%n
            if matrix[i][j] < target:
                left = mid + 1
            elif matrix[i][j] > target:
                right = mid #这个地方必须是mid
            else:
                return True
        return False