def countDigits(text):
    count = 0
    for ch in text:
        if ch.isdigit():
            count += 1
            print(ch)
    return count

def main():

    string = "23 mil 456"
    print(countDigits(string))

main()