#decorator

'''
decorators are nothing but functions that modify other functions
similar to event decorators in real life, we can also call it as
wrapper functions.

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
    
