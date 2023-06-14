leds_valores = [2, 5, 5, 4, 5, 6, 3, 7, 6, 6]
n = int(input())
for i in range(n):
    numero = input()
    total = 0
    for led in numero:
        total += leds_valores[int(led)]