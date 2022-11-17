print("Въведи число:")
num = int(input())

tuple1 = tuple()
tuple2 = tuple()

k = str(num)
for i in k:
    tuple1 += (i, )

for i in k[::-1]:
    tuple2 += (i, )

print(tuple1)
print(tuple2)
