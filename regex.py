import re

string = 'Search inside this string please'
tomatch = 'Sea'

ref = re.search('in', string) # will only check the first occ and exit
print(ref.span())
print(ref.group())

################

pattern = re.compile('in')

print(pattern.findall(string)) # will check all the occurances


################

print(re.match(tomatch, string)) # match, unlike findall will only match from the beginning of the string

###############################

regex = r"([a-x]).*?(i)"

test_str = "This is a string"

matches = re.finditer(regex, test_str, re.MULTILINE)


for matchNum, match in enumerate(matches, start=1):
    
    print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
    
    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1
        
        print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))
