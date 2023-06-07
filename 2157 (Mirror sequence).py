ncasos = int(input())

for i in range(ncasos):
    vetor = []
    e, b = map(int, input().split())
    for x in range(e, b + 1):
        vetor.append(x)
    vetor = ''.join(map(str, vetor))
    aux = vetor
    aux = ''.join(vetor)
    aux = aux[::-1]
    print(f'{vetor}{aux}')
