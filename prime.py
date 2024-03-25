# tags any, prime

d = [x 
     for x in range(1,100) 
    #  if not any(x % y == 0 for y in range(2, int(x/2) + 1))] #### THIS
     if all(x % y != 0 for y in range(2, int(x/2) + 1))] #### OR THIS
print(d)


