from random import randint
n = int(input())
print(n)
print(type(n))
a = [[randint(1, 9) for j in range(n)] for i in range(n)]
[[print(f'a [{i}][{j}] =', a[i][j]) for j in range(n)] for i in range(n)]

print(a)
