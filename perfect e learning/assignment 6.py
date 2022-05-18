print("This is the program os to reverse and sort")
array=[]
so=[]
num=int(input("How many number you want to add:-"))
for i in range(num):
    k=int(input())
    array.append(k)
so=array.sort()

print("this is the sorted array\n")
print(so)
print("this is the Reversed array\n")
for i in reversed(array):
    print(i)
