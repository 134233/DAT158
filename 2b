def BMMatch(T, P):
    m = len(P)
    n = len(T)

    i = m-1
    j = m-1

    num_comparisons = 0

    while i <= n-1:
        num_comparisons += 1
        if P[j] == T[i]:
            if j == 0:
                return "Pattern at shift position " + str(i) + " with " + str(num_comparisons/n) + \
                       " comparisons per char"
            else:
                i -= 1
                j -= 1
        else:
            i = i+m - min(j, 1 + last(T[i], P))
            j = m-1
    return "There is no substring of T matching P"

def last(c, P):
    index = -1
    for pos, char in enumerate(P):
        if c == char:
            index = pos
    return index

def main(): 
    text = "Den siste tiden har det vært ulike spekulasjoner om Russlands president Putin vil bruke atomvåpen i Ukraina. Sverre Diesen sier at Putin bør bekymre seg for at bruk av kjernevåpen vil legitimere at vestlige land går inn i krigen i Ukraina."
    pattern = "kjerne"
    result = BMMatch(text, pattern)
    print(result)
    
if __name__ == '__main__':
    main()
