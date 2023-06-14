a, b, c = map(float, input().split())
if b-c < a and b+c > a and a-c < b and a+c > b and a-b < c and a+b > c:
  print(f'Perimetro = {(a+b+c):.1f}')
else:
  print(f'Area = {(((a+b)*c)/2):.1f}')