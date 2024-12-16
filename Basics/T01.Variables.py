person_name = "Abdul Ghafoor";  # String type variable
age = 39; # number type
height = 5.6; # number with decimal points
id = 80018; # number with decimal points
is_online = True; # boolean 
# Note: python is case sensitive language True is fine true is wrong

print("Name : "+person_name);
# print("Age: "+age); #TypeError: can only concatenate str (not "int") to str
print("Age: "+str(age)); 
print(f"Height: {height}");
print("Id: %d" % id);
print("Is online: "+str(is_online));

