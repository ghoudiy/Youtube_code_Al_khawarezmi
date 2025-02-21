n = int(input())
nr = 0
for i in range(n):
  a = map(int, input().split())
  # if sum(a) >= 2:
  #   nr += 1
  nr += 1 if sum(a) >= 2 else 0
print(nr)