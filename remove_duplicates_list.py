# removing duplicated from list
# using naive methods

# initializing list
initial_list = [1, 3, 5, 6, 3, 5, 6, 1]
print("The original list is : " + str(initial_list))

result = []
for i in initial_list:
    if i not in result:
        result.append(i)

# printing after the duplicates are removed
print("The list after duplicates have been removed: " + str(result))
