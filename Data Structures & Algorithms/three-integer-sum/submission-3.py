class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()

        result=[]

        for i in range(len(nums)):

            target=-1*nums[i]

            j=i+1

            if i>0 and nums[i]==nums[i-1]:
               continue

            k=len(nums)-1

            while j<k:

                curr=nums[j]+nums[k]

                if curr<target:
                    j=j+1
                elif curr>target:
                    k=k-1
                else:
                    result.append([nums[i],nums[j],nums[k]])
                    j=j+1
                    k=k-1

                    while j<k and nums[j]==nums[j-1]:
                        j=j+1
                    
                    while j<k and nums[k]==nums[k+1]:
                        k=k-1
                    

        return result


