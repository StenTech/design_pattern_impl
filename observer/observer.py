"""
observer.py : Observer class for the Observer pattern example.
"""

class Observer:
    def __init__(self, name):
        self.name = name

    def update(self, subject):
        pass
    
class Subject:
    def __init__(self):
        self.observers = []

    def register(self, observer):
        self.observers.append(observer)

    def unregister(self, observer):
        self.observers.remove(observer)

    def notify(self):
        for observer in self.observers:
            observer.update(self)
            
class Data(Subject):
    def __init__(self):
        super().__init__()
        self._data = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
        self.notify()

     
class Logger(Observer):
    def update(self, subject):
        print(f"Logger : {subject.data}")

class Viewer(Observer):
    def update(self, subject):
        print(f"Viewer : {subject.data}")
        
if __name__ == "__main__":
    
    data = Data()
    logger = Logger("Logger")
    viewer = Viewer("Viewer")
    data.register(logger)
    data.register(viewer)
    data.data = "Some data"
    data.unregister(logger)
    data.data = "Some other data"
    data.register(logger)
    data.data = "Some more data"
    data.unregister(viewer)
    data.data = "Some final data"