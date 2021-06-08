def outerdeck_1(material):
    def innerdeck_1(function_name):
        def lastdeck_1(*args):
            print("lastdeck of outerdeck1 is acivated.",function_name.__name__,"will run now",material)
            function_name(*args)
            print("finished running everything")
        return lastdeck_1
    return innerdeck_1

def insidedeck(material1):
    def nextdeck(function_name1):
        def final(*args):
            print("final deck of insidedeck is activated.", function_name1.__name__,"will run",material1)
            function_name1(*args)
            print("finished and going back to the outerdeck")
        return final
    return nextdeck

@outerdeck_1("wood")
@insidedeck("foil")
def hello(*args):
    print(args, "hello world")

if __name__ = "__main__":
    hello("Don","George")
