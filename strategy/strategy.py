"""
strategy.py : Strategy Pattern Example
"""

class Strategy:
    def __init__(self, function=None):
        self.name = "Default Strategy"

        if function:
            self._execute = function
            
    def execute(self):
        return self._execute()
    
class Context:
    def __init__(self, strategy):
        self._strategy = strategy
        
    def execute_strategy(self):
        return self._strategy.execute()
    
class AlgorithmA(Strategy):
    def __init__(self):
        self.name = "Strategy A"
        
    def _execute(self):
        return "Strategy A is used"
    
class AlgorithmB(Strategy):
    def __init__(self):
        self.name = "Strategy B"
        
    def _execute(self):
        return "Strategy B is used"
    
if __name__ == "__main__":
    algorithm1 = AlgorithmA()
    algorithm2 = AlgorithmB()

    context = Context(algorithm1)
    context.execute_strategy()  # Output: Executing algorithm 1...

    context.strategy = algorithm2
    context.execute_strategy()  # Output: Executing algorithm 2...
