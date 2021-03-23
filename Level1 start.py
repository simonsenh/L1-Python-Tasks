#init vaiables
match_1 = 3
match_2 = 6
match_3 = 10
match_4 = 10
match_5 = 6
#creates totals
match_total = match_1 + match_2 + match_3 + match_4 + match_5
#prints results
print("On match 1 they scored {}".format(match_1))
print("On match 2 they scored {}".format(match_2))
print("On match 3 they scored {}".format(match_3))
print("On match 4 they scored {}".format(match_4))
print("On match 5 they scored {}".format(match_5))
print("In total they scored {}".format(match_total))
print("")

skin = 10
weapon = 10
vbucks = 15
giftcard_henry = 50
print("Henry has {} on his gift card".format(giftcard_henry))
giftcard_henry = giftcard_henry - skin - weapon - vbucks
print("Henry spent {} on a skin, {} on a weapon and {} on some vbucks in fortnite".format(skin, weapon, vbucks))
print("Henry has {} on his gift card".format(giftcard_henry))

#sum1ton 1
print("")
n = int(input("What is your number"))
print((n + 1) *(n / 2))

#sum1ton 2
print("")
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
