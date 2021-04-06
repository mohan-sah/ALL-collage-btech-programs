try:
    n = int(input("Enter integer:"))
    quotient = int(100*n)
    print("100*{} = {}".format(n,quotient))

except  (ValueError,ZeroDivisionError):#this ',' saves programmers time but fucks user mind. remember how calculator just use to give that one syntax error.
    print("Unable to do calculation")

print("thank you")
