sizeOfArr = int(input())
print(sorted(map(int, input().rstrip().split()))[sizeOfArr//2])