n, budget = map(int, input().split())
prices = sorted(list(map(int, input().rstrip().split())))

numToy = 0

while budget >= sum(prices[:numToy]):
    numToy += 1

print(numToy-1 if numToy > 0 else numToy)