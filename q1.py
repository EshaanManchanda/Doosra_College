#-----------------------class 1-------------------------------------
# x=input("Give input here- ")
# print(x)
# y=int(input("Give Number Here- "))
# print(y+10)
# print("hello",end="")
# print("word")
# print("Name: ",x,",Age: ",y)

#--------------------------------------class 2-------------------
from array import array
# a=5.1
# b=3
# print(a**b)
# print(a//b) 

#float output return kara ga '/' or double wala integer ta ha'//'
# print(a/b)

#conditon oprator
# x=5
# y=6
# print(x>=y)
# print(x==y)
# print(x<=y)

#assignment oprator
# c=10
# c+=20
# print(c)
# c-=20
# print(c)
# c**=x
# print(c)
# c*=x
# print(c)

#Logical
# print("-------------this is logical operator------")
# c= False
# e=not c
# if not c:
#     print("1")

    
#membership operator
# print("-------------this is Membership operator------")
# arr=[5,4,"eshaan",8.0]
# print(5 in arr)
# print(9 in arr)
# arr +=[7]
# print(arr[0])
# print(arr[-1])
# print(arr.index("eshaan"))


# print("-------------this is conditon statement------")
# var=0
# var1=100
# if var:
#     print(var)
# if var1:
#     print(var1)

# print("-------------checking even or odd------")
# num1=int(input("Enter Number: "))
# if num1%2==0:
#     print(num1,"is Even")
# else:
#     print(num1,"is odd")

#-------------------------------------day 3----------------------
# check=input("Do you want to continue 'y' or 'n':- ")
# while check=='y':
#     print("Thank you")
#     check='n'
# print("you are exit brom the loop")

# it=10
# while it>0:
#     print(it)
#     it-=1

d={"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,"i":0,"d":0,"j":0}
b=input()
print(d)
for i in b:
    if i in d:
        d[i] += 1
print(d)