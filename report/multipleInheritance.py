class One():
    def __init__(self):
        super(One, self).__init__()
        print("One, a parent!")
    def speak(self):
        print("hi from One!!")

class Two():
    def __init__(self):
        super(Two, self).__init__()
        print("Two, a parent!")
    def speak(self):
        print("hello from Two!!")

class Three(One, Two):
    def __init__(self):
        super(Three, self).__init__()
        print("Three, a child!")

obj3 = Three()
obj3.speak()

'''
super() function executes the first one it meets from left to right
as in Third(First,Second), it executed constructor of First only(in
case other classes do not have super function.

super() function in multiple inheritance executes from right to left 
as in Third(First, Second), it executes constructor of second then 
first then third. (in case other classes have super too)

in case of methods with the same name in parent classes as above:
it executes the first one it meets as in Third(First,Second),it 
executed the speak() function in First.
'''