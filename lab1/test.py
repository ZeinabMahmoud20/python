
class Human:
    def __init__(self,age):
        # self.__name=name
        self.__age=age
    @property 
    def age(self):
        return self.__age
    @age.setter
    def age(self,age):
        if age>0:
            self.__age=age
        if age<=0:
            self.__age=0

    # def getName(self):
    #     return self.__name
    
    # def sayHello(self, name=None):
 
    #     if name is not None:
    #         print 'Hello ' + name
    #     else:
    #         print 'Hello '
 
# Create instance
# obj = Human()
 
# Call the method
# obj.sayHello()
 
# Call the method with a parameter
# obj.sayHello('Guido')
man1=Human(22)
print(man1.age)
man1.age=25
print(man1.age)

man1.age=-2
print(man1.age)
# print(man1.__name__)
# print(man1.getName())