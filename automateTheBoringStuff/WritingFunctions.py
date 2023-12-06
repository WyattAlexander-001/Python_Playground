def basicHello(): # no parameters
    print('Howdy!')
    print('Howdy!!!')
    print('Hello there.')
    

def hello(name = 'Bob'): # default value
    print('Hello ' + name)

basicHello()
hello('Alice')
hello("Wyatt")
hello(str(3))

