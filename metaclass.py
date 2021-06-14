import time

def get_time(obj):
    return obj.time

class Legacy(type):
    name_list = []
    def __new__(mcs,name,base,dic):
        if "get_time" not in dic:
            dic["get_time"] = get_time
        obj = super().__new__(mcs,name,base,dic) 
        obj.time = time.ctime()
        Legacy.name_list.append(obj.__name__)
        time.sleep(1)
        return obj #this obj is a class from which we create instances.


class Legacy1(metaclass = Legacy): #obj.time is the time of creation of Legacy1 class, not the instance of this class.
    pass
class Legacy2(metaclass = Legacy): 
    pass


