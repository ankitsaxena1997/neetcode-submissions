class Solution:
    def climbStairs(self, n: int) -> int:
        
        result=[]

        result.append(1)
        result.append(2)

        if n<2:
            return result[n-1]

        for i in range(2,n):
            result.append(result[i-1]+result[i-2])
        
        return result[n-1]