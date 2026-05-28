class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        result =[]
        length=len(strs)

        dict={}

        while(len(strs)!=0):
            
            temp=[]
            temp.append(strs[0])

            j=1

            while(j<len(strs)):
                if(self.isAnagram(strs[0],strs[j])):
                    temp.append(strs[j])
                    strs.pop(j)
                else :
                    j+=1

            result.append(temp)
            strs.pop(0)
        
        return result;
    
    def isAnagram(self, s: str , t: str)-> bool:

        if len(s)!=len(t):
            return False
        
        char_dict={}

        for ch in s:
            char_dict[ch]=char_dict.get(ch,0)+1
        
        for ch in t:
            if ch not in char_dict:
                return False
            
            char_dict[ch]-=1;
            
            if(char_dict[ch]<0):
                return False

        return True