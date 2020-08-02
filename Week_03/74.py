class Solution:
    #寻找旋转排序数组中的最小值
    def findMin(self, nums: List[int]) -> int:
        left,right = 0,len(nums)-1
        res = float('inf')
        while left <= right:
            mid = (left + right)//2
            if nums[left] <= nums[mid]:
                res = min(nums[left],res)
                left = mid + 1
            else:
                res = min(nums[mid],res)
                right = mid - 1
        return res