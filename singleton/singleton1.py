# Description: Singleton pattern
def singleton(cls):
    
    # Dictionary of instances
    instances = {}
    
    # Function to get instance
    def get_instance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]
    
    return get_instance


# Class to be a singleton
@singleton
class Singleton:
    def __init__(self):
        print("Singleton created")
