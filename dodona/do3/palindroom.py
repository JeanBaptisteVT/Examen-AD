def isPalindroom(s):
    if len(s) <= 1:
        return True
    elif s[0] != s[-1]:
        return False
    else:
        return isPalindroom(s[1:-1])
