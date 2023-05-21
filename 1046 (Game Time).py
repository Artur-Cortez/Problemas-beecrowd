#minha abordagem
a, b = map(int, input().split())
if a > b:
  print(f'O JOGO DUROU {(24-a)+b} HORA(S)')
elif b > a:
  print(f'O JOGO DUROU {b-a} HORA(S)')
elif a == b:
  print('O JOGO DUROU 24 HORA(S)')

#Solução alternativa:
hi, hf = map(int, input().split())
tempo = hf - hi
if tempo <= 0:
  tempo += 24
print("O JOGO DUROU {} HORAS".format(tempo))