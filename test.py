import random
a = 10000
b = 0
t = 0
while t > 100000:
    ab = random.randint(1, 100)
    if ab == 1:
        cc = round(random.uniform(50.00, 500.00), 2)
        print(cc)
        b = b + cc
    elif ab > 1 and ab < 12:
        cc = round(random.uniform(5.00, 50.00), 2)
        print(cc)
        b = b + cc
    elif ab >= 12 and ab <= 22:
        cc = round(random.uniform(2.00, 20.00), 2)
        print(cc)
        b = b + cc
    elif ab >= 23 and ab <= 33:
        cc = round(random.uniform(1.00, 10.00), 2)
        print(cc)
        b = b + cc
    elif ab >= 98:
        cc = 1.00
        print(cc)
        b = b + cc
    else:
        cc = round(random.uniform(1.00, 2.00), 2)
        print(cc)
        b = b + cc
    if cc >= 1.1:
        a = a + 10
    else:
        a = a - 100
    t = t + 1
c = 0
d = 0
while c < 100:
    ab = random.randint(1, 1000)
    if ab <= 75:
        cc = round(random.uniform(1.00, 1.25), 2)
        d = d + cc
        print(cc)
    elif ab <= 540:
        cc = round(random.uniform(1.00, 2.00), 2)
        d = d + cc
        print(cc)
    elif ab >= 541 and ab <= 800:
        cc = round(random.uniform(2.00, 4.00), 2)
        d = d + cc
        print(cc)
    elif ab >= 802 and ab <= 915:
        cc = round(random.uniform(4.00, 8.00), 2)
        d = d + cc
        print(cc)
    elif ab >= 918 and ab <= 960:
        cc = round(random.uniform(8.00, 16.00), 2)
        d = d + cc
        print(cc)
    elif ab >= 961 and ab <= 980:
        cc = round(random.uniform(16.00, 32.00), 2)
        d = d + cc
        print(cc)
    elif ab >= 983 and ab <= 990:
        cc = round(random.uniform(32.00, 64.00), 2)
        d = d + cc
        print(cc)
    elif ab >= 991 and ab <= 996:
        cc = round(random.uniform(64.00, 128.00), 2)
        d = d + cc
        print(cc)
    elif ab == 999:
        cc = round(random.uniform(128.00, 1000.00), 2)
        d = d + cc
        print(cc)
    else:
        cc = 1.00
        d = d + cc
        print(cc)
    if cc >= 1.01:
        a = a + 1
    else:
        a = a - 100
    #else:
    #    cc = round(random.uniform(1.00, 1.50), 2)
    #    d = d + cc
    #    print(cc)
    c = c + 1
print(a)
#print(b / 10000)
#print(d / 10000)
print(d / 10)