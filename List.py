n = int(input())

s = list(i for i in range(0, n+n-1))

for i in range(0, n+n-1, 2):
    s[i] = int(input())

for i in range(1, n+n-1, 2):
    s[i] = s[i-1]+s[i+1]

print(s)
