#Operations on lists
list=[1,2,3,4]
for i in range(5,10):
    list.append(i)
print("The original list is",list)
for i in range(1,10,2):
    list.remove(i)
print("The list after removing all the odd numbers", list)
len=len(list)
i=0
j=len-1
while(i<j):
    temp=list[i]
    list[i]=list[j]
    list[j]=temp
    j-=1
    i+=1
print("After the reverse operation",list)

#Operations on tuples
tuple=(1,2,3,4,5,6,7,8,9)
for i in range(5,10):
    tuple.append(i)   #Tuples are immutable and elements cannot be appended
print("The original tuple is",tuple)
for i in range(1,10,2):
    tuple.remove(i)    #Tuples are immutable and elements cannot be deleted
print("The tuple after deletion of elements",tuple)
len=len(tuple)
i=0
j=len-1
while(i<j):
    temp=tuple[i]
    tuple[i]=tuple[j]
    tuple[j]=temp
    j-=1
    i+=1    #Tuples are immutable and element values cannot be changed
print("After the reverse operation",tuple)

#Operations on sets
set={1,2,3,4}
for i in range(5,10):
    set.add(i)  
print("The original set is",set)
for i in range(1,10,2):
    set.remove(i)    
print("The set after deletion of elements",set)
len=len(set)
i=0
j=len-1
while(i<j):
    temp=tuple[i]
    tuple[i]=tuple[j]
    tuple[j]=temp
    j-=1
    i+=1    #Sets are unordered collection and cannot be reversed
print("After the reverse operation",set)

#Operations on dictionaries
dict={'idno':'1969','name':'Kaarunya','work':'student'}
dict['location']='Hyderabad'
print("The original dictionary is",dict)
del dict['idno']
print("the dictionary after deletion of value",dict)