def smallele(arr,sn):
    arr.sort()
    k=arr[sn - 1]
    print(" the Smallest element is ",k)
def largele(arr,sn):
    arr.sort()
    k=arr[sn - 1]
    print(" the Largest element is ",k)
while True:
    print("This program is use to find out smallest element in the array by its position.")
    num=int(input("How many element you want to add: "))
    print("Please Enter your list: ")
    arr = []
    for i in range(num):
        a = int(input())
        arr.append(a)
    sn=int(input("Please enter which position you want to visit: "))
    if sn<num:
        smallele(arr,sn)
    elif sn==num:
        largele(arr, sn)

    else:
        print("You enter Wrong Value 'Please enter less than or equal to ' ",num)
    print("If you want to continue type 'y' or for exit 'n' :-")
    check = str(input())
    if check == "n":
        print("thank you for using my Program :)")
        break
    if check == "y":
        print("You Program is running")
    else:
        print("you enter wrong Keyword")
        print("thank you for using my Program :)")
        break




