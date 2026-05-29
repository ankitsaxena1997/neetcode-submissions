class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)

        if(n<=1):
            return nums

        forwardMultiplication=[0]*n
        backwardMultiplication=[0]*n
        result=[0]*n

        forwardMultiplication[0]=nums[0]
        backwardMultiplication[n-1]=nums[n-1]

        for i in range(1,n):
            forwardMultiplication[i]=nums[i]*forwardMultiplication[i-1]
            backwardMultiplication[n-i-1]=nums[n-i-1]*backwardMultiplication[n-i]

        
        result[0]=backwardMultiplication[1]
        result[n-1]=forwardMultiplication[n-2]

        for i in range(1,n-1):
            result[i]=forwardMultiplication[i-1]*backwardMultiplication[i+1]

        return result
        
