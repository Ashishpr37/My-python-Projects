letter='''
Dear <NAME>,

This letter is being written to you on <DATE>.

Regards,
Ashok Supermarket 
'''
name=input("Enter your name: ")
date=input("Enter the date of form submission: ")

letter2= letter.replace("<NAME>",name)
letter3= letter2.replace("<DATE>",date)
print(letter3)