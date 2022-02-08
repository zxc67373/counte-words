def lastRemaining(n: int) -> int:
    nlist = list(range(1, n + 1))
    flag = 0
    if len(nlist) >= 2:
        while (nlist[1] != 0):

            for i in range(0, len(nlist), 2):
                nlist[i] = 0
            flag +=1
            if (flag%2==0):
                nlist.sort(reverse=True)
            if (flag%2!=0):
                nlist.sort()
        return nlist[0]

    # elif len(nlist)==2:
    #     return nlist[1]
    else: return  1

print(lastRemaining(8))
