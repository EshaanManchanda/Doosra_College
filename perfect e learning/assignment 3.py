while True:
    num = int(input("Enter a number:"))
    fact = 1
    if num == 0:
        print(" Factorial of 0 is 1")
    elif num>0:
        for i in range(1,num+1):
            fact = fact*i
        print("The Factorial of ",i,"is ",fact)
    else:
        print("Cant do factorial for negative numbers")
    check=str(input("if you want to continue type 'y' or 'n' for exit:- "))
    if check == 'y':
        print("Program is running")
    elif check == 'n':
        print("Thank you using my program")
        print("This program is made by Eshaan Manchanda")
        break
    else:
        print("You enter wrong keyword")
        break

