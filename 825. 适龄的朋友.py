'''def numFriendRequests(ages) -> int:
    ages.sort()
    ages.reverse()
    count = 0

    for x in range(len(ages)-1):
        for y in range(len(ages)-x-1):
            if ((ages[y+x+1] <= 0.5 * ages[x] + 7) or (ages[y+x+1] > ages[x]) or (
                    ages[y+x+1] > 100 and ages[x] < 100)):
                break
            if ages[x]==ages[y+x+1]:
                count+=2
            else:
                count += 1
    return count
'''  # 暴力解题超时


class Solution:
    def numFriendRequests(self, ages) -> int:
        print(1)
        ages.sort()
        n = len(ages)
        ans = 0
        i = 0
        j = 0
        for k in range(n):
            while (i < k and (not self.check(ages[i], ages[k]))):
                i += 1
            if (j < k):
                j = k
            while (j < n and (self.check(ages[j], ages[k]))):
                j += 1
            if (j > i):
                ans += j - i - 1
        return ans

    def check(self, x: int, y: int):
        if (y <= 0.5 * x + 7 or y > x or (y > 100 and x < 100)):
            return False
        return True

ages=[16,16]
print(Solution.numFriendRequests(Solution,ages=ages))

