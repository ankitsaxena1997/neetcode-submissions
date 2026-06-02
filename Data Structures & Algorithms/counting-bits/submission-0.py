class Solution:
    def countBits(self, n: int) -> List[int]:

        result=[]
        
        for i in range(n+1):
                    
            count=0
            temp=i
            while temp:
                temp = temp & temp-1
                count+=1

            result.append(count)
        

        return result
        