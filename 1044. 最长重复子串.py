class Solution:
    def longestDupSubstring(s: str) -> str: #暴力
        ans = ''
        for i in range(len(s)):
            while s[i:i+len(ans)+1] in s[i+1:]:
                ans = s[i:i+len(ans)+1]
        return ans