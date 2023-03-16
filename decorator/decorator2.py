"""
decorator2.py : Decorator with pizza example
"""

from abc import ABC, abstractmethod

class PizzaDecorator(ABC):
    @abstractmethod
    def get_description(self):
        pass
    
    @abstractmethod
    def get_cost(self):
        pass
    

class Pizza:
    def __init__(self):
        self.description = "Pizza"
        self.cost = 10.0
        
    def get_description(self):
        return self.description

    def get_cost(self):
        return self.cost
    
    
class Cheese(PizzaDecorator):
    def __init__(self, pizza):
        self.pizza = pizza
        
    def get_description(self):
        return self.pizza.get_description() + ", Cheese"
    
    def get_cost(self):
        return self.pizza.get_cost() + 2.0
    

class Olives(PizzaDecorator):
    def __init__(self, pizza):
        self.pizza = pizza
        
    def get_description(self):
        return self.pizza.get_description() + ", Olives"
    
    def get_cost(self):
        return self.pizza.get_cost() + 1.5
    

if __name__ == "__main__":
    pizza = Pizza()
    pizza_with_cheese = Cheese(pizza)
    pizza_with_cheese_and_olives = Olives(pizza_with_cheese)

    print(pizza_with_cheese_and_olives.get_description()) # affiche "Pizza de base, fromage, olives"
    print(pizza_with_cheese_and_olives.get_cost()) # affiche 13.5

