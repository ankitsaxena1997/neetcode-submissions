class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)

        if n==1:
            return nums[0]
      
        p = 0
        q = 0
        r = 0
        s = 0

        for i in range(1,n):
            temp = max(s,r+nums[i])
            r = s
            s = temp

        for i in range(0,n-1):
            temp = max(q,p+nums[i])
            p = q
            q = temp

        return max(q,s)

        