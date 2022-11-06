'''thislist = ["apple", "banana", "cherry","mango","pine","apple"]
print(thislist[1])
print(thislist[-1])
print(thislist[2:3])     # return third item
print(thislist[2:5])     # return third forth and fifth item'''


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]      #adding new list a is present init
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)   


 ### list conferehencing

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]     ###### MAIN HIGHLIGHT CODE 

print(newlist)

