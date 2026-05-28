class Solution:

    def isAnagram(self, s: str, t: str) -> bool:

        if len(s)!=len(t):
            return False
        
        char_dict={}

        for ch in s :
            char_dict[ch]=char_dict.get(ch,0)+1
    
        for ch in t:
            if ch not in char_dict:
                return False

            char_dict[ch]-=1
                
            if char_dict[ch]<0:
                return False           
        
        return True

    

        