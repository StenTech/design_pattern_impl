"""Second implementation of the Singleton pattern.
"""

class Singleton:
    """Singleton class.
    """
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance
    
    def __init__(self):
        print("Singleton created")
    
    def some_business_logic(self):
        """Some business logic.
        """
        pass