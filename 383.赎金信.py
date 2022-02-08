class Solution:
    def canConstruct(ransomNote: str, magazine: str) -> bool:
        x=[0,0,0,0,0,0,0,0,0,0,0,0,00,0,0,0,0,0,0,0,00,00,0,0,00,0,0,0,0,0,0,0]
        y=[0,0,0,0,0,0,0,0,0,0,0,0,00,0,0,0,0,0,0,0,00,00,0,0,00,0,0,0,0,0,0,0]
        if len(ransomNote) > len(magazine):
            return False

        else:
            for i in range(len(magazine)):
                x[ord(magazine[i])-ord('a')] +=1
                if  i<len(ransomNote):
                    y[ord(ransomNote[i])-ord('a')] +=1
            for i in range(26):
                if x[i] < y[i]:
                    return False
            return True

a="aa"
b="baaaaaaaaaaaaaa"

print(Solution.canConstruct(a,b))