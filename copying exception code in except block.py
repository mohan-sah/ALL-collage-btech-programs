try:
    n = int(input("Enter integer:"))
    quotient = int(100/n)
    print("100/{} = {}".format(n,quotient))

except Exception as e:
    print("Unable to do calculation")
    print("details:",e)

print("thank you") # use of finally clause or block to just get it done with errors...haha
