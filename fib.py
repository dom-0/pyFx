def genFib(num):
  first = 0
  second = 1
  for _ in range(num):
    yield first
    temp = first + second
    first = second
    second = temp
    
for i in genFib(1000):
  print (i)

# gen dist - fixed with dt issue