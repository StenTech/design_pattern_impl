"""third version of singleton pattern
"""

class Singleton:
    
    __instance = None
    
    def get_instance(self):
        if not self.__instance:
            self.__instance = Singleton()
        return self.__instance
    
    def __init__(self):
        print("Singleton created")
        