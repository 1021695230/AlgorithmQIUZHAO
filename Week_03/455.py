class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n<0:
            n = -n
            x = 1/x
        pow = 1
        while n:
            if n&1 ==1:
                pow = pow*x
            x = x*x
            n = n>>1
        return pow