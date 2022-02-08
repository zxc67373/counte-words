def checkPerfectNumber(num: int) -> bool:
    sum = 1
    for i in range(2,num):
        if num % i == 0:
            if i*i <num:
                sum = sum + i
                sum = sum + int(num/i)
    return (sum)==num


print(checkPerfectNumber(6))
