# Tuples are often used for fixed collections of data, and their immutability makes them useful for ensuring that data remains unchanged.
my_tuple = (1,2,3)
print(my_tuple)
print(my_tuple[0])

mixed_tuple = (1,True, "String", {"name": "Abdul", "id": 18009}, 3.1415)
print(mixed_tuple)

nested_tuple = (1,2,(4,5),6)
print(nested_tuple)
print(nested_tuple[2])
print(nested_tuple[2][1])

tupe_2 = (1,2,3)
x,y,z = tupe_2
print(x,y,z)

# Tuple Operations

tuple_A = (1,2,3,1,1)
tuple_B = (5,6,7)

print(tuple_A+tuple_B); # combine
print(tuple_A[0]+tuple_B[0])
print(tuple_A*2) # repeated
print(len(tuple_A)) #length

# Tuples are Immutable

# tuple_A[0]=10 # TypeError: 'tuple' object does not support item assignment

# Tuple Methods: count, index
tuple_C = (1,2,3,1,1);
print(tuple_C.count(1)) # 3
print(tuple_C.index(1)) # 0
print(tuple_C.index(2)) # 1

# Lists and tuples are both used to store collections of items in Python, but they have significant differences. Here’s a detailed comparison:

# Aspect	                            List	                                    Tuple
# Syntax	                            Defined using square brackets [].	        Defined using parentheses ().
# Mutability	                        Mutable (can be modified).	                Immutable (cannot be modified).
# Performance	                        Slower, due to mutability.	                Faster, due to immutability.
# Usage	Used for dynamic collections.	Used for fixed or constant data.
# Methods	                            Has more methods like append, remove, etc.	Fewer methods (e.g., count, index).
# Iteration Speed	                    Slower compared to tuples.	                Faster compared to lists.
# Memory Usage	                        Consumes more memory.	                    Consumes less memory.
# Example	                            my_list = [1, 2, 3]	                        my_tuple = (1, 2, 3)