class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
    #分发饼干
        g.sort()
        s.sort()
        g_point,s_point = 0,0
        res = 0
        while g_point < len(g) and s_point < len(s):
            if g[g_point] <= s[s_point]:
                g_point += 1
                s_point += 1
                res += 1
            else:
                s_point += 1
        return res