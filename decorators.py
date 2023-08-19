def announce(f):
    def wrapper():
        print("About to run the function..")
        f()
        print("runs the function")

    return wrapper
    
@announce
def hello():
    print("hello world")


hello()