def mysuperPow(a , b):
    b.reverse()
    result = 1
    x = 0
    for i in range(len(b)):
        x = x+b[i]*pow(10,i)
    result = pow(a,(x% 1140)) % 1337
    return  result

print(mysuperPow(2,[3]))