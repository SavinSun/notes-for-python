n=eval(input())
if n==0:
    print("HL")
elif n>0:
    print("H\nL\n")
elif n<0:
    for i in "HL":
        print(i)
