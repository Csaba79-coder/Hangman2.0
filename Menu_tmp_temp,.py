

menu = {}
menu['1']="Easy level - 7 lives"
menu['2']="Medium level - 5 lives"
menu['3']="Hard level - 3 lives"
menu['quit']="Exit"
while True:
    options=menu.keys()
    options.sort()
    for entry in options:
        print(entry, menu[entry])

    selection=raw_input("Please Select:")
    if selection =='1':
      print"add"
    elif selection == '2':
      print"delete"
    elif selection == '3':
      print "find"
    elif selection == '4':
      break
    else:
      print "Unknown Option Selected!"