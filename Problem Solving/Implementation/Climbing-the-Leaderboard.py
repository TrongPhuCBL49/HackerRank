scores_count = int(input())
scores = sorted(set(map(int, input().rstrip().split())), reverse=True)
alice_count = int(input())
alice = list(map(int, input().rstrip().split()))

index = len(scores)-1
for score in alice:
    while scores[index] <= score and index != 0:
        index -= 1
    if score >= scores[0]:
        print(1)
    else:
        print(index + 2)
