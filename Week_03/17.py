class Solution:
    def canJump(self, nums: List[int]) -> bool:
    #跳跃游戏
        max_index = 0
        for i,jump in enumerate(nums):
            if max_index >= i and i + jump > max_index:
                max_index = i + jump
        return max_index >= len(nums)-1