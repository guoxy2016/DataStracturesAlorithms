def loop(chars='catdog', comp=''):
    if len(comp) == 6:
        print(comp)
    for i in chars:
        line = comp
        if i not in line:
            line += i
            loop(chars, line)


if __name__ == '__main__':
    loop()
