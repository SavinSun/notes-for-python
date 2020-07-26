#TextProBarV1.py
import time
scale = 10
print("start")
for i in range(scale):
    a = "*" * i
    b = "·" * (scale-i)
    c = i/scale * 100
    print("{:^3.0f}%[{}->{}]".format(c,a,b))
