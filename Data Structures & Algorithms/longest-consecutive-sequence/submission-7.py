class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        s = set(nums)

        max_length=0
        
        for num in s:

            current_length=1

            if num-1 not in s:
            
                while num+1 in s:
                    current_length+=1
                    num+=1
        
                max_length=max(max_length,current_length)

        return max_length
        