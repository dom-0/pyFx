my_file = open("rev.py")

# print(my_file.read())
# print("========================")

# my_file.seek(2)
# print(my_file.read())
# print("========================")
print(my_file.readline())
print("========================")
## will read from seek
print(my_file.readlines())
my_file.close()