print("Въведи число:")
num = int(input())

tuple1 = ()
tuple2 = ()

k = str(num)
for i in k:
    tuple1 += (i, )

for i in k[::-1]:
    tuple2 += (i, )

print(tuple1)
print(tuple2)
