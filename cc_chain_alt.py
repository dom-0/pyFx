travel = [('A', 'V'), ('X', 'C'), ('M', 'A'), ('V', 'X')]
dests = list(x[1] for x in travel)
path = []
for trip in travel:
    origin = trip[0]
    if origin not in dests:
        path.append(trip) # starts from here
        break
for _ in path:
    for tup in travel:
        if _[1] == tup[0]:
            path.append(tup)  # Tricky logic: Path get appended during forloop 
            break
print(path)


