class Person:
    def __init__(self, name):
        self.name = name
    def say_hi(self):
        print('Hello, how are you?', self.name)

p = Person('Swaroop')
p.say_hi()

# The previous 2 lines can also be written as
# Person().say_hi()
