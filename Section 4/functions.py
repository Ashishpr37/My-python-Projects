#We will learn about making a function
# a=3
# b=5
# c=8

# averge=(a+b+c)/3

# print(averge)

def average(): # "def keyword is very imp when defining a function()"
    i=1
    total=0
    user=int(input("How many numbers do you want to enter? : "))
    while i<=user:
        sum1=int(input(f"Enter number {i} ="))
        total=total+sum1
        i=i+1
    print(total/user)

average()