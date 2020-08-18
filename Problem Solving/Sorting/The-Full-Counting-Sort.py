n = int(input().strip())
arr = []
result = [[] for _ in range(n)]
for _ in range(n):
    arr.append(input().rstrip().split())
    if _ < n//2:
        result[int(arr[-1][0])].append('-')
    else:
        result[int(arr[-1][0])].append(arr[-1][1])
for ar in result:
    if ar != []:
        print(*ar, end=' ')
