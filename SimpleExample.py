def permute(subsetLength, mySet):
   if subsetLength == 1:
      return mySet
   else:
      return [ 
         y + x
         for y in permute(1, mySet)
         for x in permute(subsetLength - 1, mySet)
      ]

mySet = {"banane", "pere", "mere", "gutui"}
myList = list(mySet)
print(permute(1, [myList]))
print(permute(3, [myList]))
