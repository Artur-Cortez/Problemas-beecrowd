teste = list(map(float, input().split()))
teste.sort(reverse=True)
if teste[0] >= teste[1] + teste[2]:
  print("NAO FORMA TRIANGULO")
else:
  if teste[0]**2 == teste[1]**2 + teste[2]**2:
    print("TRIANGULO RETANGULO")
  if teste[0]**2 > teste[1]**2 + teste[2]**2:
    print("TRIANGULO OBTUSANGULO")
  if teste[0]**2 < teste[1]**2 + teste[2]**2:
    print("TRIANGULO ACUTANGULO")
  if teste[0] == teste[1] == teste[2]:
    print("TRIANGULO EQUILATERO")
  if (teste[0] == teste[1] or teste[1] == teste[2]) and not (teste[0] == teste[1] and teste[1] == teste[2]):
    print("TRIANGULO ISOSCELES")