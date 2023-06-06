x, y = map(int, input().split())
if x == 1:
  valor = 4
elif x == 2:
  valor = 4.50
elif x == 3:
  valor = 5
elif x == 4:
  valor = 2
elif x == 5:
  valor = 1.50
print(f'Total: R$ {(valor * y):.2f}')
