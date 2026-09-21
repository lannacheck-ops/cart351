# var_a = 330
# var_b = 200

var_a = int(input("Enter integer a:")) #converts string into interger
var_b = int(input("Enter integer b:"))
if var_b > var_a:
    print("b is greater than a")
#else statement are not indented
elif var_a>var_b:
    print("a is greater than b")
else:
    print("a == b")