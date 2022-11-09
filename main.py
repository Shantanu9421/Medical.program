def billing():
    cust = input("Customer name")
    nam = input("Enter Medicine name:")
    qu = input("Enter Quantity :")
    bil = input("Enter Amount:")
    doc = input("Recommended by :")

    ob = open("billing.txt", 'a')
    ob.write(cust + "," + nam + "," + qu + "," + bil + "," + doc + "\n")

    ob1 = open("Medicine.txt", "r")
    ls = ob1.readlines()
    ob1.close()

    i = 0
    for val in ls:
        ls1 = val.split(",")
        if ls1[0] == nam:
            a = int(ls1[1])
            b = int(qu)
            a = a - b
            print(a)
            ls1[1] = str(a)
            qu = str(qu)
            new_str = ls1[0] + "," + ls1[1] + "\n"
            ls[i] = new_str
            print("Bill Created")
        i = i+1

        ob3 = open("Medicine.txt", "w")
        ob3.writelines(ls)
        ob3.close()
    ob.close()


def medicine():
    med = input("Enter Medicine Name :")
    pri = input("Enter Quantity :")
    ob = open("Medicine.txt", "a")
    ob.write(med + "," + pri + "\n")
    ob.close()
    print("MEDICINE ADDED")


def check():
    mak = input("Enter medicine name :")
    ob = open("Medicine.txt", "r")
    loo = ob.readlines()
    for ele in loo:
        ls = ele.split(",")
        if ls[0] == mak:
            print(mak, "We Have", ls[1], "In Stock")
            break
    ob.close()


def check_customer():
    print("\t How you want to search")
    print("\t 1 - By Recommended doctor")
    print("\t 2 - By Medicine")
    ine = int(input("\tProvide Your Choice:"))
    if ine == 1:
        doc = input("\tEnter Doctor name")
        ob = open("billing.txt", "r")
        ls = ob.readlines()
        for val in ls:
            ls1 = val.split(",")
            if ls1[4] == doc + "\n":
                print(ls1[0], ls1[1], ls1[2], ls1[3], ls1[4], "\n")
        else:
            print("NO MORE DATA FOR SEARCH:")

        ob.close()

    elif ine == 2:
        me = input("\tEnter Medicine")
        ob = open("billing.txt", "r")
        ls = ob.readlines()
        for val in ls:
            ls1 = val.split(",")
            if ls1[1] == me:
                print(ls1[0], ls1[1], ls1[2], ls1[3], ls1[4], "\n")

        ob.close()


while True:
    print("1 - Billing: ")
    print("2 - Add Medicine: ")
    print("3 - Check Medicine: ")
    print("4 - Customer history: ")
    print("5 - Exit :")
    pro = int(input("Enter your choice : "))

    if pro == 1:
        billing()

    elif pro == 2:
        medicine()

    elif pro == 3:
        check()

    elif pro == 4:
        check_customer()

    elif pro == 5:
        break

    else:
        print("INVALID OPTION......")



