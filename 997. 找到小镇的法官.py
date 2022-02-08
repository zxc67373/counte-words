def findJudge(n, trust):
    innote = [0]*n
    outnote = [0]*n
    for i in range(len(trust)):
        innote[trust[i][1]-1] += 1
        outnote[trust[i][0]-1] += 1
    for i in range(n):
        if (innote[i] == n-1) and outnote[i]==0:
            return i
    else:
        return -1

n = 3
trust = [[1,3],[2,3]]
print(findJudge(n,trust))