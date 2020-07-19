class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        dict1 = {}
        for i,v in enumerate(nums):
            if target - v in dict1:
                return [dict1[target-v],i]
            else:
                dict1[v] = i

