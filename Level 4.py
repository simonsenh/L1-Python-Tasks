try:
    num_chocolate_bars=int(input("How many bars of chocolate are there? "))
    num_people=int(input("How many freinds do you have?"))
    if  num_chocolate_bars > 0:
        chocolate_bars_per_person = num_chocolate_bars // num_people
        chocolate_bars_left_over = num_chocolate_bars-(chocolate_bars_per_person * num_people)
        num_chocolate = chocolate_bars_left_over*7
        chocolate_per_person = num_chocolate // num_people
        chocolate_left_over = num_chocolate-(chocolate_per_person * num_people)
        print("Whole chocolate bars each:{}".format(chocolate_bars_per_person))
        print("Extra squares each:{}".format(chocolate_per_person))
        print("Squares left over:{}".format(chocolate_left_over))
    else:
        print("You can not have negative chocolate or negative freinds")
except ValueError:
    print("Please enter a NUMBER")
