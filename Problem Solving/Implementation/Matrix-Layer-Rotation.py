mnr = input().rstrip().split()
m, n, r = map(int, mnr)
matrix = []
for _ in range(m):
    matrix.append(list(map(int, input().rstrip().split())))
listSquares = []
for _ in range(min(m,n)//2):
    square = []
    last = matrix.pop()
    square.extend(matrix.pop(0))
    for l in matrix:
        square.append(l.pop())
    square.extend(last[::-1])
    for l in matrix[::-1]:
        square.append(l.pop(0))
    square = square[r%len(square):]+square[:r%len(square)]
    listSquares.append(square)
matrix = [[] for _ in range(m)]
for i in range(len(listSquares)):
    for x in listSquares[i][:n-i*2][::-1]:
        matrix[i].insert(i, x)
    listSquares[i] = listSquares[i][n-i*2:]
    for j in range(i+1, m-i-1):
        matrix[j].insert(i, listSquares[i].pop(0))
    for x in listSquares[i][:n-i*2]:
        matrix[m-i-1].insert(i, x)
    listSquares[i] = listSquares[i][n-i*2:]
    for j in range(i+1, m-i-1):
        matrix[j].insert(i, listSquares[i].pop())
for l in matrix:
    print(*l)
    
