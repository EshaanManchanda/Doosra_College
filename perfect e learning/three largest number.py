a=[]
num=int(input("Enter number of items you want to stored:"))
for i in range(num):
    print("Enter [0] number",i)
    item=int(input())
    a.append(item)
print(a)
a.sort()
print(a)