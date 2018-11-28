class FirstClass:
    def __init__(self, num1, num2):     # we need to use __init__ for constructor class
        self.num1 = num1
        self.num2 = num2

    def set_num1(self, num1):       # every method need to pass self
        self.num1 = num1


test = FirstClass(1, 2)  # call method __init__ and assign data to num1 and num2
test.set_num1(5)     # call method set_num1 to replace value of num 1
print(test.num1)     # result is 5
