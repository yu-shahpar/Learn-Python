#Output
print("1. Welcome to the Python tutorial created by Shahpar!\n")

#Comment 
print("2. Use the \'#' sign for comments in Python.\n")

#Print a string
print("3. To print a \'String' we have to wrap the value with either single quote or double quote, however it has to be consistent. Which means we can't mixup single and double quotes together.\n")

#variable
output_this_variable = """4. To declare a variable:
variable_name = value;
- Variable name can't start with digit or special character
- Digit can be used in any other place rather than the first character of the variable
- \'=' is known as assignment operator that assign the value to the variable.\n
"""
print(output_this_variable)

#Common Errors
print("5. Different types of common errors: \n")
syntax_error = "SyntaxError means something is wrong with the code syntax.\n"
name_error = "NameError means Python interpreter doesn't recognize the word.\n"
type_error = "TypeError means if the data type mismatches during an operation.\n"
print(syntax_error + name_error + type_error)

#Arithmetic Operations
print("6. Five common operations using arithmetics are +, -, *, /, % \n")
an_int = 100
another_int = 10
print("Let's assume we have two variables, an_int = 100, another_int = 10\n")
print("The add operation looks like: str(an_int + another_int)" + str(an_int + another_int))
print("The substract operation looks like: str(an_int - another_int)" + str(an_int - another_int))
print("The multiplication operation looks like: str(an_int * another_int)" +str(an_int * another_int))
print("The division operation looks like: str(an_int / another_int)" + str(an_int / another_int))
print("The modulo (remainder) operation looks like: str(an_int % another_int)" + str(an_int % another_int) + "\n")



#List

#How to create a list?
list_1 = ["Shahpar", 7, "Instructor"]
#print(list_1)

#List can contain multiple data types
list_2 = ["Shahpar", 7, True, 180.0]

#If we plan to fill out later then we can create an empty list
list_3 = []

#Manipulation

#To add a new element to the end
list_3.append("New Element")
#print(list_3)

