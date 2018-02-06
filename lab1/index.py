def displayIndex(word,letter):
  indexList=[]
  start=-1
  for s in word:
      start=start+1
      if s is letter:
        index=word.index(s,start)
      #   index=word.enumerate(s)
      #   print(s)
        indexList.append(index)
  return indexList
# print(index)
# word.replace(vowel,"")


if __name__ == '__main__':
  pass
  word=input("Enter your string ")
  letter=input("Which letter do you want to search index ")
  print(displayIndex(word,letter))