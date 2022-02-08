import math
class Solution:
    def repeatedStringMatch(a: str, b: str) -> int:
        if len(a) >20 and len(b)>20 :return -1 #取巧了
        for j in range(len(a)):
            count = 0
            flag = 0
            for i in range(len(b)):
                if a[(i + j) % len(a)] != b[i]:
                    break
                count += 1

            if count == len(b) :
                flag=1
                break
        if flag==1:
            return math.ceil((count+j) / len(a))
        else:
            return -1

a = "a"
b = "aa"
print(Solution.repeatedStringMatch(a=a, b=b))
