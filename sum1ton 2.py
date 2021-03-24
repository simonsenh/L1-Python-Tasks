#sum1ton 2
yes = 1
no = 1
maybe = 0
while maybe < 12:
    maybe = 1 + maybe
    yes = 1
    while yes < 13:
         print("{} * {} = {}".format(yes,maybe ,no))
         yes += 1
         no = yes * maybe
