list = [10,20,30,40]           #another is to use reverse
l = []
for i in list:
    l.insert(0,i)
 
print(l)


#using temp
def swapList(newlist):
    size = len(newlist)
    
    
    #for swapping
    temp = newlist[0]
    newlist[0] = newlist[size - 1]
    newlist[size - 1] = temp
    return newlist
newlist = [10,200,30,40,60]
print(swapList(newlist))

#last and first element index
def SwapList(newList):
    #for swapping
    newList[0],newList[-1] = newList[-1],newList[0]
    return newList
newList = [90,60,1020,20]
print(SwapList(newList))

#using pop append insert method
def SWAPLIST(NEWLIST):
    first = NEWLIST.pop(0)
    second = NEWLIST.pop(-1)
    NEWLIST.insert(0,second)
    NEWLIST.append(first)
    return NEWLIST

list = [5,6,7,9]


print(SWAPLIST(list))
    
    
    
    