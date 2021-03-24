b = 1
a = 2
c = 1
n = int(input("What is your number"))
while c <= n:
    c += 1
    a = 2
    while a <= n:
        if c * a == n:
            b = 2
        a = a + 1
if n == 1:
    b = 2
if b == 2:
   print("It is not a prime number")
if b == 1:
   print("It is a prime number")
#This code will only go up to around 4 digits numbers any higher and the code will take longer than 15 seconds.
