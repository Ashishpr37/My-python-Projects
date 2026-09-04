a="78" # the value of a is a string

print(a,type(a)) # 78 <class 'str'>

# I will make a new variable and put the value of 'a' in it

b = float(a) # float is a function. float is converting value of a into a float value and the value is saved in 'b' variable

print (b, type(b)) #78.0 <class 'float'>


#----------------------------------------X----------------------------------------------------

#string to integer type conversion
print("\nWelcome to String to integer converter : " )
print ("Pls NOTE :- string should be a number because the str conversion doesn't apply on invalid values like having a character in between or at first or at last or anywhere")
t=input("\nEnter the string : ")

print  ("This is the string that you entered - ",t, "\nTo confirm this is the type of value - ", type(t))

s = int(t)

print("\nThe entered string now has been converted into an integer value")

print("The converted value is this - ",s,"\nThe type of this value is this : ",type(s))