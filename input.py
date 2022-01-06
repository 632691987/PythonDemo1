myage = input("please input your age:   ")
print("your age is", myage)

if int(myage) > 20:
    print("more than 20")


if myage.isnumeric():
    print("it is a number")