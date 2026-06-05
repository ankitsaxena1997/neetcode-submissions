class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        carry_over=0

        if(digits[len(digits)-1]==9):
           digits[len(digits)-1]=0
           carry_over=1

        if carry_over==0:
            digits[len(digits)-1]+=1
            return digits
        
        for i in range(len(digits)-2,-1,-1):

            if carry_over==0:
                return digits
            else :
                if digits[i]!=9:
                    carry_over=0
                    digits[i]=digits[i]+1
                else :
                    digits[i]=0
        
        if carry_over==1:
            digits.insert(0,1)
        
        return digits
        