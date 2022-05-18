arr = [];
print("Please Enter how many number you want to add:- ");
num=int(input());
for n in range(num):
    print("Enter number",n+1)
    k=int(input());
    arr.append(k);
print("Duplicate elements in given array: ")
for i in range(0, len(arr)):
    for j in range(i + 1, len(arr)):
        if (arr[i] == arr[j]):
            print(arr[j]);