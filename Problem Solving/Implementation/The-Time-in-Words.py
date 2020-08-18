numbers = [None, "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", None, "sixteen", "seventeen", "eighteen", "nineteen", "twenty"]

numbers.extend(["twenty " + number for number in numbers[1:10] ])
wordNumbers = dict(enumerate(numbers))

h = int(input())
m = int(input())

if m == 0:
    print(wordNumbers[h], "o' clock")
elif m == 30:
    print("half past", wordNumbers[h])
elif m == 15:
    print("quarter past", wordNumbers[h])
elif m == 45:
    print("quarter to", wordNumbers[h+1])
elif m == 1:
    print("one minute past", wordNumbers[h])
elif m>30:
    print(wordNumbers[60-m], "minutes to", wordNumbers[h+1])
else:
    print(wordNumbers[m], "minutes past", wordNumbers[h])
