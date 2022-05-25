import random

def randRange(a,b,c,d):
    #creating an array to hold all the values between two numbers
    arr = []
    #this will be an array we shuffle to get a random number each time
    randarr = []
    #adding the low limit to our array
    arr.append(b)
    while b <= c:
        b = b + .0001
        #rounding floating points to 4 decimal places
        arr.append(round(b, 4))

    for i in range(0, d):
        #shuffling the array
        random.shuffle(arr)
        #adding our random number to the list and printing for LMT use ;)
        randarr.append(arr[0])
    print(randarr)

randRange(.0005, .0003, .0004, 25)