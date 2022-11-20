num = int(input("Въведи число: "))

L = lambda x:x*2+1
print("Нечетни числа:")

for k in range(num):
    print(L(k), end=" ")
print("\nКвадрати на числата:")

for k in range(num):
    print((lambda x:x*x) (k+1), end=" ")
