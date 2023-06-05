while True:
  n = int(input())
  if n == 0: break

  for i in range(n):
    a, b, c, d, e = map(int, input().split())
    cont, letra = 0, ''
    if a <= 127: cont+=1
    letra = "A"
    elif b <= 127: cont+=1
    letra = "B"
    elif c <= 127: cont +=1
    letra = "C"
    elif d <= 127: cont += 1
    letra = "D"
    elif e <= 127: cont +=1
    letra = "E"
    elif cont == 0 or cont > 1: print("*")
    
    