class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}
        max_len=0
        left=0
            
        for i in range(len(s)):

            if s[i] in last_seen and last_seen.get(s[i])>=left:
                left=last_seen.get(s[i])+1
            
            curr_len=i-left+1
            max_len=max(curr_len,max_len)
            
            last_seen[s[i]]=i   

        return max_len





        