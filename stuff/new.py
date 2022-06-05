dic = {}



print("If you want to print the dictonary enter Print")
print("To end program use CTRL C")



try:
  while True:
    user = input("Input 2 words please: ")
    if user =="Print":
      print("Program ended by Print command")
      print(dic)
      quit()



    user = user.split()

    if len(user) != 2:
      print("Only two words are accepted")



    elif user[0] not in dic:
      dic[user[0]] = [user[1]]

    else:
      dic[user[0]] = dic[user[0]] + [user[1]]



except KeyboardInterrupt:
  print ("Program ended with CTRL C")
  print(dic)