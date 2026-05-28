class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_dict = {}

        for num in nums:
            num_dict[num]=num_dict.get(num,0)+1
        
        sorted_dict = sorted(num_dict.items(), key = lambda x:x[1] , reverse = True)

        result=[]

        for i in range(k):
            result.append(sorted_dict[i][0])
        
        return result
        