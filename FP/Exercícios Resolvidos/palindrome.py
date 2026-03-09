def ispalindrome(s):
    return s == s[::-1]

def isPalindromo(frase):
    revstr = ""
    for char in range(len(frase)-1, -1, -1):
        revstr += frase[char]

    if revstr == frase:
        return True
    else:
        return False


print(ispalindrome("ana"))      # True
print(ispalindrome("osso"))     # True
print(ispalindrome("radar"))    # True
print(ispalindrome("python"))   # False

print("A partir daqui é a segunda função")

print(isPalindromo("ana"))      # True
print(isPalindromo("osso"))     # True
print(isPalindromo("radar"))    # True
print(isPalindromo("python"))   # False
