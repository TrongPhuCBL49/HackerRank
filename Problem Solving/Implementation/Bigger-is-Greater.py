for T_itr in range(int(input())):
    w = input()
    i = len(w)-1
    while w[i]<=w[i-1] and i>0:
        i -= 1
    if i == 0:
        print('no answer')
    else:
        j = len(w)-1
        while w[j]<=w[i-1]:
            j -= 1
        behind = [c for c in w[i-1:j]+w[j+1:]]
        behind.sort()
        print(w[:i-1]+w[j], end='')
        print(*behind, sep='')
