n = 4
count = 0
while n > 0:
    print(n)
    n -= 1
    count += 1
print("Este loop foi executado {} vezes e este {} é o n final".format(count, n))
print(" ")

n = 1
count = 0
while n < 1000:
    print(n)
    n *= 2
    count += 1
print("Este loop foi executado {} vezes e este {} é o n final".format(count, n))
print(" ")

count = 0
for n in (1, 2, 5, 10, 20, 50):
    print(n)
    count += 1
print("Este loop foi executado {} vezes e este {} é o n final".format(count, n))
print(" ")

count = 0
for c in "abracadabra":
    print(c)
    count += 1
print("Este loop foi executado {} vezes e este {} é o c final".format(count, c))
print(" ")

count = 0
for n in range(10):
    print(n)
    count += 1
print("Este loop foi executado {} vezes e este {} é o n final".format(count, n))
print(" ")

count = 0
for n in range(10, 0, -2):
    print(n)
    count += 1
print("Este loop foi executado {} vezes e este {} é o n final".format(count, n))
print(" ")