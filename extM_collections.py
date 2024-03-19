from collections import Counter, OrderedDict

# Hashmap, counts the occurances 
a = "There are twice the amount of hex in a string than normal end-flow objects"
x = [1,1,2,3,3,1,4,5,12,23,51,4,2]
print(Counter(a))
print(Counter(x))

# ordered dictionary, dict.
# from py 3.7 dictionaries are ordered anyway, so this is obsolete or used for version earlier than 3.7
d = OrderedDict()
d['a'] = 1
d['b'] = 2
d['c'] = 3
print(d)