print("Въведи цяло число:")
num = int(input())

list1 = []

for i in range(1, num+1):
    list1.append(i)
print("Списък:", list1)

list2 = list1[::-1]

list3 = {list1[i]:list2[i] for i in range(num)}

print("Речник:", list3)
