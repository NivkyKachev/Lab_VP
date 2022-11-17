print("Въведи текст:")
txt = str(input())

key = dict()

for i in txt:
    if i in key:
        key[i] += 1
    else:
        key[i] = 1

print(key)
