def sort_array(s):
    def inner(n):
        if n < 0:
            return
        if s[n] % 2 != 0:
            for i in range(n, len(s)-1):
                s[i], s[i+1] = s[i+1], s[i]
            # s.append(s[n])
            # s.pop(n)

        inner(n - 1)

    inner(len(s)-1)


if __name__ == '__main__':
    ss = [int(i) for i in '1357924680']
    sort_array(ss)
    print(ss)
