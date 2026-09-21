# a comment in python 
# single line comments
# print("this is correct")
# print(25+30/7) # float division (with decimal points)
# print(25+30//7) # interger division (rounded number)
# print(100-25*3%4)
# print(7.3==5)

# bool_var_a=True
# bool_var_b= False
# bool_var_c= False

# not_a = not(bool_var_a) #will return false cuz bool a is true
# and_a_b = bool_var_a and bool_var_b #will return false because bool a is true and bool b is false so false takes predecence and the varibale returns false. However if the statement was "or" at least one of the booleans need to be true to return true
# testVar = 5
# print(type(testVar)) #Returns what type of variable the content is. this variable returns "int" cuz testVar contains 5.

# my_name = "Sabine"
# my_fav_fruit = "kiwi"
# saved_str = f"my favorite fruit is {my_fav_fruit}"
# print(f"my favorite fruit is {my_fav_fruit}")#formated string


my_name = input("Name: ")#waits for input to be entered
my_fav_fruit =  input("Fav Fruit: ")
my_fav_animal = input("Fav Animal: ")
my_fav_veg = input ("Fav Veg: ")
my_fav_color = input ("Fav Color: ")
a_saved_fstring = f"Your fav fruit is {my_fav_fruit}"

print(f"Your name is {my_name}")
print(f"Your favorite color is {my_fav_color} and You also love {my_fav_animal}s")
print(a_saved_fstring)