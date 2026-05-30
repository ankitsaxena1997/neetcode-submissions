class Solution:
    def isPalindrome(self, s: str) -> bool:

        final_s="".join(char for char in s if char.isalnum())

        final_s= final_s.lower()
        length= len(final_s)

        i=0
        j=length-1

        while i<=j :
            if final_s[i]!= final_s[j]:
                return False
            i=i+1
            j=j-1
        
        return True
        