soma = 0
x = int(input())
y = int(input())
if x > y:
  for i in range(y+1,x):
    if i % 2 != 0:
      soma += i
elif x < y:
  for i in range(x+1, y):
    if i % 2 != 0:
      soma += i
print(soma)