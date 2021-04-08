
#sum1ton 1 by henry simonsen on 1/3/2021

#Gets number from user
try:
    n=int(input("What is your number (positive integer)? "))
    #test int is positive
    if n > 0:
        #Outputs sum of all numbers under the choosen number
        print((n + 1) * (n / 2))
    else:
        print("Not a negative!!!!!!")
except ValueError:
    print("Please input a number between integer >0 ")





