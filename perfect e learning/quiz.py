# Write a program to prompt the user for days and rate per day to compute total pay. Use 50 days and
# a rate of 3.5 per day to test the program. Total pay is equal to (days* Rate per day). You should use inpu
# t to read a string and float() to convert the string to a number. Don't worry about error checking or bad us
# er data. Good Job!`
def computepay(h, r):
    if h > 40:
        p = 1.5 * r * (h - 40) + (40 * r)
    else:
        p = h * r
    return p


hrs = input("Enter Hours:")
hr = float(hrs)
rphrs = input("Enter rate per hour:")
rphr = float(rphrs)

p = computepay(hr, rphr)
print(p)


