print("This program is used to find out the price of work")
rate=int(input("Enter price per day "))
days=int(input("Enter Number of days "))
i=r(rate,days);
print("Ther price to pay :",i)
def r(ra,da):
    i=ra*da
    return i