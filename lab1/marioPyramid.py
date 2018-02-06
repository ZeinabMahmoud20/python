number=input("Enter your number  ")
range1=range(int(number))
#this for is for looping outer number of lines
# for i in range1: 
#     print(" "*(int(number)-i) +"*"*(i+1) )

for n in range(int(number)):
    print(" "*(int(number)-n)+"*"*(n+1))
