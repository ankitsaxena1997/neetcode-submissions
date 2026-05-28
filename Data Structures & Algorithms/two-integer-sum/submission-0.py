class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        numsMap={}

        for i in range(len(nums)):

            if(target-nums[i] in numsMap):
                return [numsMap.get(target-nums[i]) , i]
            else:
                numsMap[nums[i]]=i
        
        return 
            