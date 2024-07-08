def demo():
    print('print demo')

def hello():
    print('inside hello')
    demo()

demo() #demo() dependant call
print()
hello() #indepent call
