class Solution:
    def reverse(self, x: int) -> int:
        sign=-1 if x<0 else 1
        x=abs(x)
        n=0
        while x!=0:
            r = x % 10
            n = n*10 + r
            x = x // 10
            # 32-bit signed integer overflow check
        if n < -2**31 or n > 2**31 - 1:
            return 0
        return sign * n

c=Solution()
print(c.reverse(564))