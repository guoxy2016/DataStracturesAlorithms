def reverse(s):
    def inner(n, l):
        if n < l:
            ch = inner(n+1, l)
            return ch + s[n]
        else:
            return ''
    return inner(0, len(s))


if __name__ == '__main__':
    print(reverse('pots&pans'))
