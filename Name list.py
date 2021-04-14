name_list = ["Evi", "Madeleine", "Dan", "Kelsey", "Cayden", "Hayley", "Darian"]
print("The list of names is {}".format(name_list))
print("The list of names in alphabetical order {}".format(sorted(name_list)))
user_name = input("What is your name?")
if user_name in name_list:
    print("Your name is in the list!!!:(")
else:
    print("Your name is not in the list")
    Replace_name = input("What name would you like to replace?")
    if Replace_name in name_list:
      place = name_list.index(Replace_name)
      name_list[place] = user_name
      print(name_list)
      new_name = input("What name would you like to add?")
      name_list.append(new_name)
      print(name_list)
    else:
     print("This is not a name in the list!!!:(")
