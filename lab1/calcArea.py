import math
def calcArea(type,num1,num2=1):
    # type=input("Enter the first letter of the Geo Shape of ('T','R','C','S') ")
    if type =='t' or type=='T':
        # base=int(input("Enter Base! "))
        # tHeight=int(input("Enter Height! "))
        area= 0.5*num1*num2
        print("Triangle area is ",area)
    elif type =='r' or type=='R':
        # widht=int(input("Enter Width! "))
        # rHeight=int(input("Enter Height! "))
        area= num1*num2
        print("Rectangle area is ",area)
    elif type =='c' or type=='C':
        # raduis=int(input("Enter Number! "))
        area=math.pi*(num1**2)
        print("Circle area is ",area)
    elif type =='s' or type=='S':
        # Number=int(input("Enter Number! "))
        area=num1**2
        print("Square area is ",area)
    else: 
        area=0
        print("Sorry wrong letter!")
    return area
if __name__ == '__main__':
  pass
  type=input("Enter the first letter of the Geo Shape of ('T','R','C','S') ")
  
  if type=='t' or type=='T' or type=='r' or type=='R':
    num1=input("Enter Number 1 : ")
    num2=input("Enter Number 2 : ")
  elif type=='c' or type=='C' or type=='s' or type=='S':
    num2=1
    num1=input("Enter Number 1 : ")
  else:
    num1=num2=0
  print(calcArea(type,int(num1),int(num2)))