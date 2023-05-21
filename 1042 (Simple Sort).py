numeros = list(map(int, input().split()))
backup = numeros.copy()
numeros.sort()
for i in numeros:
  print(i)
print()  
for x in backup:
  print(x)