while True:
  x1, y1, x2, y2 = map(int, input().split())
  movimentos = 0
  if x1 + x2 + y1 + y2 == 0: break
  # caso linha reta
  elif x1 == x2 and y1 == y2: movimentos = 0
  elif x1 == x2 or y1 == y2:
    movimentos = 1       
  elif x1 - x2 == y1 - y2 or x2 - x1 == y2 - y1 or x1 - x2 == y2 - y1 or x2 - x1 == y1 - y2:
    movimentos = 1
  else:
    movimentos = 2
  print(movimentos)