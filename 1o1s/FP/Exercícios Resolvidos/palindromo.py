def isPalindrome(string):
    inversed = string [::-1]
    #print(inversed)
    
    if string == inversed:
        return True
    else:
        return False

def main():
    string = input("Palavra: ")
    print(isPalindrome(string))

main()