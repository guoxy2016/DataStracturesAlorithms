def palindrome(s):
    def inner(start, stop):
        if start < stop:
            if s[start] == s[stop]:
                return inner(start + 1, stop - 1)
            else:
                return False
        else:
            return True

    return inner(0, len(s) - 1)


if __name__ == '__main__':
    print(palindrome('racecar'))
