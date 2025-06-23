x = int(input("Enter a number : "))

match x:
    case 100:
        print("x is 100")

    case 200:
        print("x is 200")

    case _ if 1<= x <=10:
        print("x lies between 1 and 10")

    case nm:
        print("x does not match")

    