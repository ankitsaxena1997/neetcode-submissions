class Solution:

    def isAnagram(self, s: str, t: str) -> bool:

        if len(s)!=len(t):
            return False
        
        char_dict={}

        for ch in s :
            char_dict[ch]=char_dict.get(ch,0)+1
    
        for ch in t:
            if ch in char_dict:
                char_dict[ch]=char_dict[ch]-1
                if char_dict[ch]<0:
                    return False
            else:
                return False
        
        return True

    

        