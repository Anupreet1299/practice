"""

technologies = ["AI", "hadoop", "android", "JEE"]
technologies[1]= "mobile apps"  #update operation/set operation

print(technologies)

#del(technologies[1])

print(technologies[1:3])

print(technologies[1:-2])
"""

data = [1, 2, 3, 4, 5, "john", "jenny", "joe", "john"]
#data.pop(3) #deletes data on the basis of index
#print(data)

data.remove(3) #removes the matching element
print(data)

data.remove("john")  
print(data)