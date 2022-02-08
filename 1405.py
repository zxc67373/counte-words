def longestDiverseString(a: int, b: int, c: int) -> str:
    num = {"a": a, "b": b, "c": c}
    num = sorted(num.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)
    result = ''
    while True:
        for i in num:
            if i[1]<=0 :
                return result
            if len(result)>=2 and result[-2:] ==i[0] * 2:
                continue
            result += i[0]
            i[1] -=1
            break

    return result