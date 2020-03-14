usernameInput = input("Username : ")
passwordInput = input("Password : ")
if usernameInput=="admin" and passwordInput=="1234":
    print("----------------------------------------------")
    print("           Wellcome to YAYASHOP               ")
    print("----------------------------------------------")
    print("Please Select :")
    print("1.Coffee   : 60 THB")
    print("2.Tea      : 30 THB")
    print("3.Lemon Tea: 40 THB")
    print("4.Orange Juice: 50 THB")
    orderSelected=int(input("Please order : "))
    if 0 < orderSelected <= 4:
        orderAmount=int(input("Amount : "))
        if orderAmount !="":
            if orderSelected == 1:
                print("Total (THB) = ",60*orderAmount)
            elif orderSelected == 2:
                print("Total (THB) = ", 30 * orderAmount)
            elif orderSelected == 3:
                print("Total (THB) = ", 40 * orderAmount)
            elif orderSelected == 4:
                print("Total (THB) = ", 50 * orderAmount)
        else:
            orderAmount = input("Amount : ")
    elif orderSelected>4:
        print("None Item")
    else:
        orderSelected = input("Please order : ")
else:
    print("Error!!!")
