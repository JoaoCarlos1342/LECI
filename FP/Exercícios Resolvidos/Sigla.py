def shorten(name):
    short = ""
    for char in name:
        if char.isupper():
            short += char
    return short

def main():
    print(shorten("Universidade de Aveiro"))
    print(shorten("United Nations Organazation"))

    return 0

main()