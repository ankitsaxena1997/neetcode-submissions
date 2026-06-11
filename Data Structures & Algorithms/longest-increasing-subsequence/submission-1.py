class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        n = len(nums)
        dp = [1]*n

        for i in range(1,n):

            j=i-1

            while j>=0 :
                
                if nums[j]<nums[i]:
                    dp[i]=max(dp[i],dp[j]+1)

                elif nums[j]==nums[i]:
                    dp[i]=max(dp[i],dp[j])
                
                j = j-1
        
        result = 1

        print(dp)

        for val in dp:
            result = max(result , val)
        
        return result


        