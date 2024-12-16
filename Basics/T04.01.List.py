# Empty list
empty_list = []
print("-------------------------------------")
print("---------Numbers---------")
numbers = [1,2,3,4,5]
print(numbers)

print("-------------------------------------")
print("---------Mixed---------")
mixed = [2.5,"Malik",3,4,5, True]
print(mixed)

print("-------------------------------------")
print("---------Nested---------")
nested = [[1,2],[3,4]]
print(nested)

print("-------------------------------------")
print("---------Accessing Items---------")
numbers = [1,2,3,4,5]
print(numbers[0])
print(numbers[-1]) # last item

print("-------------------------------------")
print("---------Add items---------")
numbers[1] = 22
print(numbers)
numbers.append(6) #Adds 6 to the end
print(numbers)
numbers.insert(1,7)
numbers.insert(2,7)
print(numbers)

print("-------------------------------------")
print("---------Remove items---------")

numbers.pop() #Removes the last item
print(numbers)

numbers.remove(7) # Removes the first occurrence of 7
print(numbers)

del numbers[0] # Deletes the item at index 0
print(numbers)

print("-------------------------------------")
print("---------List Methods---------")

numbers = [3, 1, 4, 1, 5]
numbers.sort()         # Sorts the list
print(numbers)  
numbers.reverse()      # Reverses the list
print(numbers)  
# numbers.count(1)       # Counts occurrences of 1
print(numbers.count(1))  
numbers.extend([9, 2]) # Adds multiple items
print(numbers)         # Output: [5, 4, 3, 2, 1, 9]