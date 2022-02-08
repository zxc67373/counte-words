def dayOfTheWeek(day: int, month: int, year: int) -> str:
    monthday = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]
    week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    days = 0
    days +=365*(year-1971)+(year-1969)//4  # "//" 结果取整
    days += sum(monthday[:month - 1])
    if (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)) and month >= 3:
        days+=1
    days +=day
    return week[(days+3)%7]
