import random
big = "ABCDEFGHIJKLMNOPQRSTWXYZ"
small = "abcdefghijklmnopqrstwxyz"
symbol = ("@#*$~")
number = "0123456789"
name = str(input(" Put any name: "))

all = big + small + symbol + number
length = int(input("""Password lenght: 
Note: This lenght will be added after your name """))
Password = "".join(random.sample(all,length))
print("Your Random Password Is: ", name +Password)
