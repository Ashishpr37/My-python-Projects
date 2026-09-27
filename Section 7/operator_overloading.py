'''
What is Operator Overloading?

Operator overloading means:

Giving an operator such as +, -, *, ==, <, etc. a special meaning when it is used with your own objects.

Overloading = making something work in different ways depending on what you use it with.

For example, Python already knows:

5 + 3

means:

8

And:

"Hello " + "World"

means:

Hello World

The same + operator behaves differently depending on the data.

That's operator overloading.




2. But how does Python do this?

Python uses special methods called dunder methods.

Dunder = "double underscore."

For example:

__add__()

is the special method behind +.

So when you write:

a + b

Python internally uses something similar to:

a.__add__(b)

You normally don't call __add__() yourself.

3. Example with your own class

Suppose we create:

class Number:
    def __init__(self, value):
        self.value = value

Now:

num1 = Number(10)
num2 = Number(20)

print(num1 + num2)

This doesn't automatically work the way we want.

Why?

Python doesn't know what + should mean when you're adding two Number objects.

So we can tell Python what + should do.

class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value


num1 = Number(10)
num2 = Number(20)

print(num1 + num2)

Output:

30


we write the overloading operator in the class as method
'''



'''
Create a class called Box.

The class should have:

length
width

For example:

box1 = Box(10, 5)
box2 = Box(3, 2)

Now overload the + operator so that:

box1 + box2

creates a new Box whose:

length = box1.length + box2.length
width = box1.width + box2.width

So:

box1 + box2

should produce a box with:

length = 13
width = 7
'''


class Box:
    def __init__(self, length, width):
        self.length=length
        self.width=width

    def __add__(self, other):
        total_length=self.length + other.length
        total_width=self.width + other.width

        return Box(total_length, total_width)

b1=Box(10, 6)
b2=Box(12, 7)

b3=b1+b2
