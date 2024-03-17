### Data pipeline of HUGE records / files using generators
### This allows memory to NOT be filled up
### taken a list "lines" as an example but could be replaced with a file
### file_name = "techcrunch.csv"
### lines = (line for line in open(file_name))
###
### Find the sum of all funds with Type A
### Tags: large file, largefile, xls, csv, pipelines, generator

lines = [
    "Type,col2,col3,col4,col5,col6,col7,col8,fund",
    "A,is,something,I,am,not,aware,code.kraft,9",
    "B,this,does,not,get,qualified,sorry,huh,12",
    "A,welcome,and,toto,lol,iti,ba,huh,15"
]

listsoflist = (x.rstrip().split(',') for x in lines)
print(listsoflist)
cols = next(listsoflist)
info_dicts = (dict(zip(cols, x)) for x in listsoflist)

# print(cols)
# print(next(info_dicts))
# print(next(info_dicts))
# print(next(info_dicts))

funding = (int(rec['fund']) for rec in info_dicts if rec['Type'] == "A")

print(sum(funding))

