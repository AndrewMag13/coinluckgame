import random
b = 1000
c = 0
k = 3
while c < 100000:
    if k == 3:
        a = random.randint(1,99)
        if a <= 25:
            b = b + 3
        else:
            b = b - 1
        c = c + 1
        print(b)

print(b)