class Solution:

    def isHappy(self, n: int) -> bool:

        last_seen= set()  
        
        while n!=1 :

            sum=0
            while n!=0 :
                sum+= (n%10)**2
                n=n//10
            
            n=sum

            if sum in last_seen:
                return False
            else:
                last_seen.add(sum)
        
        return True


        

        
        