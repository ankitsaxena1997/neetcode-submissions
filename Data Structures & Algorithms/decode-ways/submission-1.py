class Solution:
    def numDecodings(self, s: str) -> int:

        str_set = set()

        for i in range(1,27):
            str_set.add(str(i))

        dp = [0]*(len(s)+1)

        dp[0]=1
        
        if s[0]=='0':
            return 0
        else :
            dp[1]=1
        
        for i in range(1,len(s)):
            
            flag=0
            if s[i-1:i+1] in str_set:
                if str(s[i]) in str_set:
                    dp[i+1]=dp[i-1]+dp[i]
                else:
                    dp[i+1]=dp[i-1]
            else:
                if str(s[i]) in str_set:
                    dp[i+1]=dp[i]
                else:
                    return 0

        return dp[len(s)]

        