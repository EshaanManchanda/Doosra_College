while True:
    print("Simple calculator By Tech Love V")
    print("------------------------------------------")
    print("These are the Arthmatical Opration :-")
    print("1. Add '+' ")
    print("2. Subtraction '-' ")
    print("3. Multiplication '*' ")
    print("4. Division '/' ")
    print("5. Modulus '%' ")
    print("6. Exponentiation '**' ")
    print("7. Floor division '//' ")
    print("8. Exit '000'")
    check=input(":- ")
    if check=='1' or check=='+' or check=="add":
        while True:
            print("Enter Numbers Here or Exit=000")
            num1=float(input())
            if num1==000 :
                break
            num2=float(input())
            print(num1,"+",num2,"=",num1+num2)
            
        print("\n-----------------------------------------------\n")
    elif check=='2' or check=='-' or check=="subtraction":
        while True:
            print("Enter Numbers Here or Exit=000")
            num1=float(input())
            if num1==000:
                break
            num2=float(input())
            print(num1,"-",num2,"=",num1-num2)
            print("\n-----------------------------------------------\n")
    elif check=='3' or check=='*' or check=="multiplication":
        while True:
            print("Enter Numbers Here or Exit=000")
            num1=float(input())
            if num1==000:
                    break
            num2=float(input())
            print(num1,"*",num2,"=",num1*num2)
        print("\n-----------------------------------------------\n")
    elif check=='4' or check=='/' or check=="Division":
        while True:
            print("Enter Numbers Here or Exit=000")
            num1=float(input())
            if num1==000:
                    break
            num2=float(input())
            print(num1,"/",num2,"=",num1/num2)
        print("\n-----------------------------------------------\n")
    elif check=='5' or check=='%' or check=="modulus":
        while True:
            print("Enter Numbers Here or Exit=000")
            num1=float(input())
            if num1==000:
                    break
            num2=float(input())
            print(num1,"%",num2,"=",num1%num2)
        print("\n-----------------------------------------------\n")
    elif check=='6' or check=='**' or check=="exponentiation":
        while True:
            print("Enter Numbers Here or Exit=000")
            num1=float(input())
            if num1==000:
                    break
            num2=float(input())
            print(num1,"**",num2,"=",num1**num2)
        print("\n-----------------------------------------------\n")
    elif check=='7' or check=='//' or check=="Floor":
        while True:
            print("Enter Numbers Here or Exit=000")
            num1=float(input())
            if num1==000:
                    break
            num2=int(input())
            print(num1,"//",num2,"=",num1//num2)
        print("\n-----------------------------------------------\n")
    elif check=='8' or  check=="exit" or check=='000':
        exit()
    else:
        print("Invalid Action!")