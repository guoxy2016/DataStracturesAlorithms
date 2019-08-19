from decimal import Decimal


def change():
    give, pay = input('请输入`支付金 售价`, 使用空格隔开例如"20 13.50"\n').split()
    give, pay = map(Decimal, [give, pay])
    if give < pay:
        print('您支付的金额不足!')
        return
    money = give - pay
    # money = round(money, 1)
    result = f'找钱:{money}\n'
    give_change = {}
    for c in map(Decimal, ['100', '50', '20', '10', '5', '1', '0.5', '0.1']):
        num = money // c
        # print('num', num)
        if num != 0:
            give_change[str(c)] = int(num)
        money -= num * c
    # print('give_change', give_change)
    for k, v in give_change.items():
        result += '%3s元的纸币%s张\n' % (k, v)
    print(result)


if __name__ == '__main__':
    while True:
        try:
            change()
        except (EOFError, ValueError):
            break
