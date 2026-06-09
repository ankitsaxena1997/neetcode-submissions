class Solution:
    def longestPalindrome(self, s: str) -> str:

        memo = {}

        def solve(s):

            if s in memo:
                return memo[s]

            if self.isPalindrome(s):
                memo[s]=s
                return s

            str1 = solve(s[0:-1])
            str2 = solve(s[1:])
        

            if len(str1) > len(str2):
                memo[s]=str1
            else:
                memo[s]=str2
            
            return memo[s]
        
        return solve(s)

    
    def isPalindrome(self, s: str):
        return s==s[::-1]

        



            
                



        