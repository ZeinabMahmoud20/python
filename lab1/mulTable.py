
def mulTable(num):
    start=end=1
    list1Inner=[]
    listOuter=[]

    if end <= int(num):
        for n in range(1,int(num)+1):
            for m in range(1,n+1):
                #  print(n*m)
                list1Inner.append(n*m)
            listOuter.append(list1Inner)
            list1Inner=[]

    # print(listOuter) 
    return listOuter


if __name__ == '__main__':
#   pass
  number= input("Enter number ")
  print(mulTable(number))