class Solution:
    def dayOfYear(date: str) -> int:
        year = int(date[0:4])
        mounth = int(date[5:7])
        day = int(date[8:10])
        dayofyear = 0
        for i in range(mounth):
            if i == 1: dayofyear += 31
            if i == 2:
                if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:dayofyear += 29
                else: dayofyear+=28
            if i == 3: dayofyear += 31
            if i == 4: dayofyear += 30
            if i == 5: dayofyear += 31
            if i == 6: dayofyear += 30
            if i == 7: dayofyear += 31
            if i == 8: dayofyear += 31
            if i == 9: dayofyear += 30
            if i == 10: dayofyear += 31
            if i == 11: dayofyear += 30
            if i == 12: dayofyear += 31
        return dayofyear+day

date = "2019-01-09"
print(Solution.dayOfYear(date=date))




