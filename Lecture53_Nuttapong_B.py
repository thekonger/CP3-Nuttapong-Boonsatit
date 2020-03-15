def vatCal(totalPrice):
    result=totalPrice+(totalPrice*7/100)
    return result

totalPrice=float(input("Price = "))
print(vatCal(totalPrice))