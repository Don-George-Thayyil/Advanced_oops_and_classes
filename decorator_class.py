
class decorator:
    def __init__(self, hobby):
        self.hobby = hobby
    def __call__(self, the_function):
        def wrapper(*args,**kwargs):
            the_function(*args,**kwargs)
            print(f"My hobby is {self.hobby}")
        return wrapper

@decorator("playing Volleyball")
def hello_world(*args,**kwargs):
    print(f"Hello! My name is {args[0]}")

if __name__ == "__main__":
    hello_world("Don George")

