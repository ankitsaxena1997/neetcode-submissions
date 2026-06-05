class Solution:

    def isHappy(self, n: int) -> bool:

        seen= set()  
        
        while n!=1 :

            total=0
            while n!=0 :
                total+= (n%10)**2
                n=n//10
            
            n=total

            if n in seen:
                return False
            else:
                seen.add(n)
        
        return True


        

        
        