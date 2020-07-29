class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #前K个高频元素
        dict1 = {}
        res = []
        for i in nums:
            dict1[i] = dict1.get(i,0)+1
        a = sorted(dict1.items(),key = lambda x:x[1],reverse = True)
        for i in range(len(a)):
            res.append(a[i][0])
        return res[:k]