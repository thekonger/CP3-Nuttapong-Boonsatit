menuList=[]
priceList=[]
def showBill():
    print("-----Food Shop-----")
    sum=0
    for num in range(len(menuList)):
        print(menuList[num],priceList[num])
        sum += int(priceList[num])
    print("---------------------")
    print("Total",sum)
while True:
    menuName=input("Please enter menu : ")
    if menuName.lower()=='exit':
        break
    else:
        menuPrice=input("Price : ")
        menuList.append(menuName)
        priceList.append(menuPrice)
showBill()

