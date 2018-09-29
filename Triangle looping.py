num=int(input("Enter number: ")) #This is used to input numbers to loop.

for a in range(0, num): #a is for columns.
    for b in range(0, a+1):  #b is for "*"
        print("*", end="") #the end printing is to make columns.
    print() #another row
#bottom-left side

for c in range(0, num): #c is for columns.
    for d in range(0, num-c): #d is for spacing
        print("", end="*")
    for e in range(0, c+1): #e is for "*"
        print("*", end="")
    print() #another rows
#Top left side

for f in range(0, num): #f is for columns.
    for g in range(0, num-f): #g is for "*"
        print("*", end="") #the end printing is to make columns
    print() #another rows
#Top right side

for h in range(0, num): #h is for columns
    for i in range(0, h+1): #i is for spacings
        print("", end="") #the end printing is to make columns
    for j in range(0, num-h): #j is for "*"
        print("*", num-h)
    print() #another row
#pyramid-shaped looping

for k in range(1, num): #k is for columns
    for l in range(1, num-k): #l is for spacings
        print("", end="") #the end printing is to make columns
    for m in range(k*2-1, 0, -1): #m is for "*"
        print("*", end="") #another rows
    print() #another column
#diamond-shaped looping

for n in range(1, num): #n is for columns
    for o in range(1, num-n): #o is for spacings
        print("", end="") #the end printing is to make columns
    for p in range(n*2-1, 0, -1):
        print("*", end="") #f is for "*"
    print() #another column
#pyramid-shaped looping

for q in range(1, num-1): #this is for reversal pyramid-shaped looping
    for r in range(1, q+1):
        print("", end="")
    for s in range(((num-1)*2-1)-q*2, 0, 1):
        print("*", end="")
    print() #another row