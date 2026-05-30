class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        t = {}
        max_len=0
        last_index=0
            
        for i in range(len(s)):

            if s[i] in t and t.get(s[i])>=last_index:
                last_index=t.get(s[i])+1
            else :
                curr_len=i-last_index+1
                max_len=max(curr_len,max_len)
            
            t[s[i]]=i   

        return max_len





        