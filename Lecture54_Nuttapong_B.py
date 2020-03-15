def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput=="u" and passwordInput=="123":
        return True
    else:
        return False
def showMeno():
    print("--------------------------------")
    print("1. Vat Calculator")
    print("2. Price Calculator")

def menuSelected():
    userSelected = int(input(">>"))
    return userSelected
def vatCalculate(totalPrice):
    vat=7
    result=totalPrice+(totalPrice*vat/100)
    return result
def priceCalculate():
    price1=int(input("First product price : "))
    price2=int(input("Second product price : "))
    vatCalculate(price1 + price2)
    return vatCalculate(price1+price2)

if login()==True:
    while True:
        showMeno()
        numMenu=menuSelected()
        if numMenu==1:
            totalPrice=int(input("Price = "))
            print("Total Price = ",vatCalculate(totalPrice))
        elif numMenu==2:
            print("Total Price = ",vatCalculate(priceCalculate()))
else:
    print("Error")
