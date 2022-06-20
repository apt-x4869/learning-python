x = [1, "DevOps", "test", 3, 4, 5, 6, 7]
y = [ "Aman", "Devops", "test", "term", "python"]
print(type(x[0]))
print(type(x[1]))

print(x)

# Access a list element
print(x[2])

# Access index which is not present
# print(x[9])

# Lenght of List
print("length of x : ")
print(len(x))

print("length of y : ")
print(len(y))

#Append into list/ Add a element at last
x.append("extra")
x.append("extra")
print(x)

# Insert into list
x.insert(2, "tom" )
x.insert(2, "extra")
print(x)

# Remove elment
x.remove("tom")
print(x)

# Remove from last remove
x.pop()
print(x)

# Count number of similar element
x.append("test")
x.append("tom")
x.append("extra")
print(x)
print ( "No of extra : " + str(x.count("extra")) )
print ( x.count("test") )

# Reverse a List 
y = [ 3, 2, 1 , 4, 5, 6, 9]
print(y)
y.reverse()
print(y)

# Sort a List
y.sort()
print(y)

# Clear the List
#x.clear()
#print(x)