rooms=[762,819,608]
for i in rooms:
  last_digit=i%10
  first_digit = i//100
  if first_digit+last_digit < 10:
    print(i)