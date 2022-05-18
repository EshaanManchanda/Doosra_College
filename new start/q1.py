# num1 = input("Enter number of cases: ")
# num2 = input("Enter number of cases: ")
# num3 = input("Enter number of cases: ")
# num4 = input("Enter number of cases: ")
# num5 = input("Enter number of cases: ")
# sum = float(num1+num2+num3+num4+num5)
# avg = sum/5;
# print("Avrage",avg);
i=0;
sum=0;
while(i<5):
    num1 = input("Enter number of cases: ");
    i=i+1;
    sum=sum+float(num1)

avg = sum/5;
print("Avrage",avg);
