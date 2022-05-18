def ctp(days,rate):
    pay=days*rate
    return pay
xd=input("Enter Days")
xr=input("Enter Rate")
try:
    fd=float(xd)
    fr=float(xr)
    print("Pay:",ctp(fd,fr))

except:
    print("Error, Please enter numeric input")