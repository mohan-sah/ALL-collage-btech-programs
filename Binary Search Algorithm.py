array=[1,2,3,4,6,7,8,9,10,12,13]#get the sorted list
low = 0
high = len(array) - 1           # define high and lows
key = int(input("enter search key"))
while (low <= high):    # keep shorting list to its half every single time and also it depends .hahaha
    middle = int((low + high) / 2)
    if (key == array[middle]):
        print("key found at position:", middle)
        break
    elif(key < array[middle]):
        high = middle - 1   #change lows and highs middle position
    else:
        low = middle + 1;
if(low > high):
    print("key not found")


