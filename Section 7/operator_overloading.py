'''
Create a class called Student.

Each student should have:

name
marks

For example:

s1 = Student("Rahul", 80)
s2 = Student("Aman", 70)
Part 1 — Overload +

Make:

s3 = s1 + s2

create a new Student object where:

name = "Combined"
marks = s1.marks + s2.marks

So:

s3 = s1 + s2

should produce a student like:

Name: Combined
Marks: 150

You'll need:

def __add__(self, other):

Part 2 — Overload ==

Make it possible to compare two students:

s1 == s2

The result should be True if their marks are equal, otherwise False.

You'll need:

def __eq__(self, other):
Expected behavior
s1 = Student("Rahul", 80)
s2 = Student("Aman", 70)
s3 = s1 + s2

print(s3.name)
print(s3.marks)

print(s1 == s2)

Expected output:

Combined
150
False
'''

class Student:
    def __init__(self, name, marks):
        self.name=name
        self.marks=marks


    def __add__(self,other):
        
        return Student("combined",self.marks+other.marks)

    def __eq__(self, other):
        return self.marks==other.marks
        


s1=Student("Abhi",60)
s2=Student("Abhijeet",60)

s3=s1+s2
print(s3.name)
print(s3.marks)
print(s1==s2)
