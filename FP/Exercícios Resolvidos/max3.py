n1 = float(input("number? "))
n2 = float(input("number? "))
n3 = float(input("number? "))
mx = 0.0

'''
if n1 > n2 & n1 > n3:
    print("Maximum: {}".format(n1))
elif n2 > n1 & n2 > n3:
    print("Maximum: {}".format(n2))
else:
    print("Maximum: {}".format(n3))
'''

if n1 > n2:
    mx = n1
elif mx > n3:
    print("Maximum: {}".format(mx))
else:
    print("Maximum: {}".format(n3))