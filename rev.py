num = int(input("Enter the number to reverse: "))

revnum =  int(str(num)[::-1])
if revnum == num: print ("Palidrome!!!")
else: print ("Nope!!!")