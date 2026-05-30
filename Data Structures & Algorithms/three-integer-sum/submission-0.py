class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()

        result=[]

        for i in range(len(nums)):

            target=-1*nums[i]

            j=i+1
            k=len(nums)-1

            while j<k:

                curr=nums[j]+nums[k]

                if curr<target:
                    j=j+1
                elif curr>target:
                    k=k-1
                else:
                    temp=[nums[i],nums[j],nums[k]]
                    if temp not in result:
                        result.append(temp)
                    j=j+1
                    k=k-1

        return result


