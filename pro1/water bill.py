def bill():
    print("Last_reading -")
    lr=int(input())
    print("Current_reading")
    cr=int(input())
    print("No of days")
    nod=int(input())
    r=cr-lr
    e=r*1000
    sr=667
    d=nod*sr
    rs=e-d
    s=0
    print("Reading - ",e)
    print(" itani honi chaia ",d)
    print("kitani jyada aai ya kam aai",rs)
    if(rs<=0):
        print("bill  zero hai",s)
    else:
        rs = r * 23
        s = rs
        print("Bill jyada hai",s)
    print("you want to reapate ")
    go=str(input())
    if(go=="yes"):
        bill()
    else:

      quit()
bill()
quit()



