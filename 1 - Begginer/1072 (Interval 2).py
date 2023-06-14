dentro = 0
fora = 0
n = int(input())
for i in range(n):
  a = int(input())
  if a >= 10 and a <= 20:
    dentro += 1
  else: fora += 1
print('{} in'.format(dentro))
print('{} out'.format(fora))