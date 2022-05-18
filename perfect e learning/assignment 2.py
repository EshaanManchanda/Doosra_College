def sumfun(a):
  cum_sum=[]
  for i in range(len(a)):
    cum_sum.append(sum(a[:i+1]))
  print("you cumulative sum is = ")
  print(cum_sum)
while True:
  print("Write a function to take a list as input and return the list of cumulative sums of the respective list.")
  print("please enter how many Number you want to enter")
  num=int(input())
  print("Please enter your list:-")
  list=[]
  for i in range(num):
    a=int(input())
    list.append(a)
  print("You enter these items")
  print(list)
  sumfun(list)
  print("If you want to continue type 'y' or for exit 'n' :-")
  check=str(input())
  if check=="n":
    print("thank you for using my Program :)")
    break
  if check=="y":
    print("You Program is running")
  else:
    print("you enter wrong Keyword")
    print("thank you for using my Program :)")
    break

