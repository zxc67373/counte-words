def truncateSentence(s: str, k: int) -> str:
    countblock=0
    for i in range(len(s)):
        if s[i] ==' ':
            countblock= countblock+1
        if countblock == k-1:
            return s[:i]