##try-except
##try-except-else
##try-except-else-finally


try:
    print(10/0)
except ZeroDivisionError as zex:
    print(zex.__cause__)
else:
    print("OK, pass case")
finally:
    print("End")