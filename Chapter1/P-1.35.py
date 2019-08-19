import random

month = range(1, 13)
day = range(1, 31)
seq = []
for m in month:
    if m == 2:
        for d in range(1, 30):
            seq.append('%02d%02d' % (m, d))
    elif m in [1, 3, 5, 7, 8, 10, 12]:
        for d in range(1, 32):
            seq.append('%02d%02d' % (m, d))
    else:
        for d in range(1, 31):
            seq.append('%02d%02d' % (m, d))
for p in range(5, 101, 5):
    temp = 0
    t = 1000
    for i in range(t):
        dates = []
        have = False
        for j in range(p):
            date = random.choice(seq)
            if date not in dates:
                dates.append(date)
            else:
                have = True
        if have:
            temp += 1
    print(temp / t)
