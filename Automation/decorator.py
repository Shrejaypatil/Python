#decorator

'''
decorators are nothing but functions that modify other functions
similar to event decorators in real life, we can also call it as
wrapper functions.

concepts covered:

nested func
func as parameters
decorators
@wrapper functions
decorator chaining

'''

def event_decorator(func):
    def inner_func():
        print("Adding lights")
        func()
    return inner_func
    

@event_decorator   
def stage():
    print("Hello Adding stage")
    
stage()
    
# manager = event_decorator(stage)

# manager()

#decorator chaining

'''
we can use multiple decorators, the innner most will run first
'''


def star(func):
    def innner():
        print("*"*20)
        func()
        print("*"*20)
        
    return innner
    

def dollar(func):
    def inner():
        print("$"*20)
        func()
        print("$"*20)
        
    return inner
    
    
@star
@dollar
def printer():
    print("Hello world!")

printer()
