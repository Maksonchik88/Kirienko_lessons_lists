text = input().split()
for i in range(1, len(text)):
    if int(text[i]) > int(text[i - 1]):
        print(text[i], end=' ')
