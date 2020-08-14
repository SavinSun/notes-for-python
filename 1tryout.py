b = []
a = input()
for i in a[::1]:
    if  65 <= ord(i) <= 90 :
        b.append(i)
print(b)