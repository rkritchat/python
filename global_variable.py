letter = "kritchat"               # This is global variable

print(letter)


def change_name(name):
    letter = name               # I try to reassign value of global variable
    print(letter)               # then print, result is "Rojanaphruk"


change_name("Rojanaphruk")      # call method chane_name to reassign value of global variable

print(letter)                   # Try to print global variable but it still print "kritchat"


def change_global_variable(name):
    global letter                   # Fix by using global key, I need to tell python that hey python
    letter = name                   # this is global variable, let change it bro!


change_global_variable("ABCV")      # Change global variable
print(letter)                       # Result is "ABCV"

