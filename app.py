# project imports
from utils.constants import INTRO


# print Hello World!
print("Hello World!")


# create float variable
float_var = float(0.1)
print(type(float_var))


# create a string variable
str_var = str("This is a string variable")
print(type(str_var))


# create a function that asks for user's name and prints it with a sentence, "Hello, my name is {user}!" with f strings.
def get_user_name():
    """
    Takes name from the user through input and outputs it with, "Hello, my name is {user}!"
    """
    # run this block of code till we get a valid input
    while True:
        user_name = input("Please enter your name: ")
        try:
            if user_name is "":
                print("Please enter your name below.")
            else:
                len_of_user_name = len(user_name)
                first_three_chars = list(user_name)[:3]
                return [f"{INTRO}{str(user_name).capitalize()}!", first_three_chars]
        except:
            print("Please enter a valid name!")

# assigning a variable to the output of the function
get_user_name_output = get_user_name()
# print the name of the user
print(get_user_name_output[0])

# print first 3 characters of the user_name
print("The first three characters in user_name are")

if len(get_user_name_output[1]) < 3:
    print("Note: The user_name has less than 3 characters!")

for char in list(get_user_name_output[1]):
    print(char)


# math calculation
math_calculation = (((1+5)*7)+6)
length_of_math_calculation = len(str(math_calculation))
print("The maths calculation (((1+5)*7)+6) is " + str(math_calculation))

# print the string variable
display_str_var = len(str_var)
print("The length of string variable str_var is " + str(display_str_var))


lst = [1, 2, 41, 23, 4, 212, 2]
# print the list in reverse
rev_list = lst[::-1]
print("The list -> " + str(lst) + " in reverse is: " + str(rev_list))

# return a sublist which has numbers less than the number entered by the user.
# run this block of code till we get a valid input
while True:
    num = input("Enter a number: ")
    # new list which will have the numbers less than the number entered by the user
    new_lst = []
    try:
        if num is "":
            print("Please enter a number!")
        else:
            num = float(num)
            new_lst = filter((lambda x: float(x) < num), lst)
            print("The new list which has values less than " + str(num) + " is \n" + str(list(new_lst)))
            break
    except ValueError:
        print("Please enter a valid number!")
