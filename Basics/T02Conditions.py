print('---------If Condition---------')
is_online = True;
x = 5;
if is_online:
    print("Person is online")
if x < 5:
    print('X is less than 5')
elif x>5:
    print('X is greater than 5')
else:
    print("X is 5")

print('-------------------------------------')
print('---------Nested If Condition---------')

y=10;

if x==5:
   if y==10:
       print("Nested if is working")
print('-------------------------------------')
print('---------if with Logical Operators---------')

if x==5 and y==10:
    print("Logical AND")

print('-------------------------------------')
print('---------Multiple Statements in single if---------')

if x==5:
    print("X==5")
    print("X is less than 10")





