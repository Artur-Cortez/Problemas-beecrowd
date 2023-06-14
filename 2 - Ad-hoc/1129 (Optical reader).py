while True:
  n = int(input())
  if n == 0: break

  for i in range(n):
    a, b, c, d, e = map(int, input().split())

    if a <= 127 and b > 127 and c > 127 and d > 127 and e > 127: print("A")
    elif a > 127 and b <= 127 and c > 127 and d > 127 and e > 127: print("B")
    elif a > 127 and b > 127 and c <= 127 and d > 127 and e > 127: print("C")
    elif a > 127 and b > 127 and c > 127 and d <= 127 and e > 127: print("D")
    elif a > 127 and b > 127 and c > 127 and d > 127 and e <= 127: print("E")
    else: print("*")
    