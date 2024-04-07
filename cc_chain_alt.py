travel = [('A', 'V'), ('X', 'C'), ('M', 'A'), ('V', 'X')]
dests = list(x[1] for x in travel)


path = list(filter(lambda x: x[0] not in dests, travel))



for _ in path:
    for tup in travel:
        if _[1] == tup[0]:
            path.append(tup)  # Tricky logic: Path get appended during forloop 
            break
print(path)


