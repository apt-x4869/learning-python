tests  = ["test1", 2, "test3", "test4", "test5", "test6"]

for i in tests:
    print("The element is : " + str(i) )
    print(type(i))


even = 0

for x in range(0,100):
    if x%2 == 0:
        even = even + 1

print(even)


# For 1st loop
# i in tests (i = test1)
# print(i) ==> print(test1)

# For 2nd Loop
# i in tests (i = 2 )
# print(i) ==> print(test2)
# type(i) --> int

