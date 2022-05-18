def length(num):
    num_string=str(num)
    lenght=len(num_string)
    print("The length of number :-",lenght)

def sum_num(num):
    sum=0;
    for n in str(num):
        sum +=int(n)
    print("This is the sum of the number:-",sum)

print("This fumction is help you to find you the size and sum of the given number")
print("Enter your number:- ")
num=int(input())
length(num)
sum_num(num)