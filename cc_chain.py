travel = [('A', 'V'), ('X', 'C'), ('M', 'A'), ('V', 'X')]

# solve the path followed

# first find out where to begin from
# then create the chain

secondary = list(map((lambda x: x[1]), travel))
path = list(filter((lambda x: x[0] not in secondary), travel))
# path is where he starts from

for _ in travel:
  position = path[-1] # holding the last travelled tuple
  for sub_items in travel:
    if position[1] == sub_items[0]:
      path.append(sub_items)
      break

print(path)