b = ("")
a = 2
c = 1
n = int(input("What is your number"))
while c <= n:
    c += 1
    a = 2
    while a <= n:
        if c * a == n:
            b = ("not")
        a = a + 1
if n == 1:
    b = ("not")
print("It is {} a prime number".format(b))
