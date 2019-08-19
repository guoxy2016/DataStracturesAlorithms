# # pot + pan = bib        p, o, t, a, n, b, i
# # boy + girl = baby      b, o, y, g, i, r, l, a
# from itertools import permutations
# num = 0
# for item in permutations('0123456789', 7):
#     p, o, t, a, n, b, i = item
#     fir = p + o + t
#     sec = p + a + n
#     res = b + i + b
#     if int(fir) + int(sec) == int(res):
#         num += 1
#         print('pot+pan=bib\n%s+%s=%s' % (fir, sec, res))
# print(n)

num = 0


def puzzle(kk, ss, nn):
    for ii in ss:
        nn.append(ii)
        ss.remove(ii)
        if kk == 1:
            # print(nn)
            # p, o, t, a, n, b, i = nn
            # # print(p, o, t, a, n, b, i)
            # pot = int(p + o + t)
            # # print(pot)
            # pan = int(p + a + n)
            # # print(pan)
            # bib = int(b + i + b)
            # # print(bib)
            # if pot + pan == bib:
            #     # print('pot=%03d\npan=%03d\nbib=%03d' % (pot, pan, bib))
            #     print('%03d + %03d = %03d' % (pot, pan, bib))

            b, o, y, g, i, r, l, a = nn
            boy = int(b + o + y)
            girl = int(g+i+r+l)
            baby = int(b+a+b+y)
            if boy + girl == baby:
                print('%03d + %04d = %04d' % (boy, girl, baby))
        else:
            puzzle(kk - 1, ss.copy(), nn)
        ss.add(ii)
        nn.remove(ii)


if __name__ == '__main__':
    puzzle(8, set('1234567890'), [])
    print(num)
# 497 + 3650 = 4147
# 457 + 3690 = 4147
