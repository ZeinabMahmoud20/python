def sortDict(names):

    result={}
    for item in names:
        if item[0] in result:
            result[item[0]].append(item)
        else:
            result[item[0]]=[item]
    return result


if __name__ == '__main__':
  pass
  values={"Alaa","Mona","Zainab"}
#   values=raw_input("Enter a list of items")
  print(sortDict(values))


     