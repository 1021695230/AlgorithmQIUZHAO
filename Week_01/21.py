class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1[m:] = nums2
        for right in range(m,m+n):
            target = nums1[right]
            for left in range(right):
                if target <= nums1[left]:
                    nums1[left+1:right+1] = nums1[left:right]
                    nums1[left] = target
        return nums1