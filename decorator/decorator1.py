"""
decorator.py : Decorator design pattern implementation in Python
"""

from abc import ABC, abstractmethod


class ImageComponent(ABC):
    
    @abstractmethod
    def operation(self):
        pass
    
class Image(ImageComponent):
    
    def __init__(self, filename):
        self._filename = filename
        
    def operation(self):
        print("Displaying image {}".format(self._filename))
        
class ColorFilter(ImageComponent):
    def __init__(self, image):
        self._image = image
        
    def operation(self):
        self._image.operation()
        print("Applying color filter")
        
class BlurFilter(ImageComponent):
    def __init__(self, image):
        self._image = image
        
    def operation(self):
        self._image.operation()
        print("Applying blur filter")
        
        
if __name__ == "__main__":
    base_image = Image("image.jpg")
    filtered_image = ColorFilter(base_image)
    blurred_image = BlurFilter(filtered_image)

    blurred_image.operation() # affiche "Image de base sans effet appliqué", "Ajout du filtre de couleur", "Ajout de l'effet de flou"

