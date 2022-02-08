def uncommonFromSentences(s1: str, s2: str):
    result = []
    j = 0
    k=0
    lenth = len(s1) if len(s1) > len(s2) else len(s2)
    for i in range(lenth+1):

        if (i < len(s1) and s1[i] == ' ') or i == len(s1):
            if not s1[j:i] in s2  and not s1[j:i] in s1[i:]:
                result.append(s1[j:i])
                if i == len(s1) and s1[j:i] in s1[:j]:
                    result.pop(len(result)-1)

            j = i + 1

        if (i < len(s2) and s2[i] == ' ') or i == len(s2):
            if not s2[k:i] in s1 and not s2[k:i] in s2[i:]:
                result.append(s2[k:i])
                if i == len(s2) and s2[k:i] in s2[:j]:
                    result.pop(len(result)-1)
            k = i + 1

    return result


print(uncommonFromSentences("apple apple","banana"))