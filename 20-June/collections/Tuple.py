# Tuple

# They are ordered
# You can't change value for a tuple

t = ("apple", "mango", "hello","deops", "hello")

print(type(t))
print(t)
print(len(t))
#print(dir(t))

# Count number of any element
number = t.count("mango")
print(number)

# Find index of an element 
print(t.index("hello"))

t[0] = "aman"