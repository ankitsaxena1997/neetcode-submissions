class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_dict = {}

        for num in nums:
            num_dict[num]=num_dict.get(num,0)+1
        
        sorted_dict = sorted(num_dict.items(), key = lambda x:x[1] , reverse = True)

        result=[]


        for key , value in sorted_dict:
            if(k>0):
                result.append(key)
                k-=1
        
        return result
        