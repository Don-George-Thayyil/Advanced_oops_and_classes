class LuxuryWatches:
    __watches_created = 0
    def __init__(self):
        LuxuryWatches.__watches_created += 1
    
    @classmethod
    def get_number_of_watches_created(cls):
        return cls.__watches_created
    
    @classmethod
    def engraving(cls,engrave):
        if cls.check(engrave) :
            _watch = cls()
            _watch.text = engrave
        else:
            raise ValueError(engrave, "Only alphabets and numbers are allowed.")
    @staticmethod
    def check(engrave):        
        if engrave.isalnum() and len(engrave) <= 40:
            return True            
if __name__ == "__main__":
    watch2 = LuxuryWatches.engraving("dongeorge")
    print(LuxuryWatches.get_number_of_watches_created())

