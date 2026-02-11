n = int(input())

while n > 0:
    word = input()
    size = len(word)
    if size > 10:
        c1 = word[0]
        c2 = word[-1]
        print(c1+str(size-2)+c2)
    else:
        print(word)
    n -= 1