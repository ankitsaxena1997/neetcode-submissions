class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums)<2:
            return len(nums)

        nums.sort()

        j=0

        max_length=1
        current_length=1

        while(j<len(nums)):

            if (nums[j]==nums[j-1]+1):
                current_length+=1
            elif(nums[j]!=nums[j-1]) :
                current_length=1
            
            j=j+1
            
            max_length= max(max_length, current_length)

        return max_length


