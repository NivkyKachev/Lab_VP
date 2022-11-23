def polindrom(num):
    resul = str(num) == str(num)[::-1]
    if resul:
        # Ако числото е палиндром.
        return 1
    else:
        # Ако числото НЕ Е палиндром.
        return 0

num = int(input("Enter a number: "))

print(polindrom(num))
