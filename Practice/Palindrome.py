
def palindrome(str):

    if len(str) >= 2:
        if str[0] != str[-1]:
            return False
        else:
            return palindrome(str[1:-1])

    else:
        return True


print(palindrome("rotor"))
print(palindrome("motor"))
