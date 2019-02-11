import array as ar

n = ar.array('i',[23,45,12,45,67])
#print(n)

for i in n:
    print(i)
    
print("to access index")

for i in range(len(n)):
    print(i,n[i])
    
print("array can also be accessed using negative indexing")
print(n[-1])
print(n[-5])

print("array slicing")
print(n[1:4])
print(n[:])
print(n[:5])
print(n[2:])
print(n[-5:])
print(n[:-3])

print("change array element values")
n[0] = 10
print(n)

#n[1:3] = [2,4] TypeError: can only assign array (not "list") to array slice
n[1:3] = ar.array('i',[2,3])
print(n)
