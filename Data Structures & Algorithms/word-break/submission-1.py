class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        if s in wordDict:
            return True
        
        index_list = []
        index_list.append(0)

        for i in range(1,len(s)+1):

            for idx in index_list:

                if s[idx:i] in wordDict:
                    index_list.append(i)
                    break
            
        if len(s) in index_list:
            return True
        
        return False
        