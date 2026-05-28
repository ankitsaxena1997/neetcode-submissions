class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_dict={}
        for ch in s :
            if ch in char_dict:
                char_dict[ch]=char_dict[ch]+1
            else :
                char_dict[ch]=1;
    
        for ch in t:
            if ch in char_dict:
                if char_dict[ch]>0:
                    char_dict[ch]=char_dict[ch]-1
                else:
                    return False
            else:
                return False
        
        for key in char_dict:
            if(char_dict[key]!=0):
                return False
        
        return True

    

        