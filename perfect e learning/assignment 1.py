print("This is the program to find out the total numbers of vowels in the Statement");
print("Please Enter your statement:-");
count=0;
std=str(input())
if std=="":
    print("This is default Satement")
    std="no one in brief history of computing has ever written a piece of perfect software"
    print(std)
else:
    std=std.lower();
for word in std:
    for letter in word:
        if letter=="a" or letter=="e" or letter =="i" or letter=="o" or letter=="u":
            count+=1;
print(count);
if count==0:
    print("There is no Vowels.");