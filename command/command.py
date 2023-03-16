"""
command.py : Command pattern implementation for Python
"""

class Command:
    def execute(self):
        pass
    
    def undo(self):
        pass
    
    
    
class Invoker:
    def __init__(self):
        self._history : list[Command] = []
        
    def execute(self, command: Command):
        command.execute()
        self._history.append(command)
        
    def undo(self):
        if len(self._history) > 0:
            self._history.pop().undo()


class Receiver:
    
    def action1(self):
        print("Receiver executiong action 1...")
    
    def action2(self):
        print("Receiver executiong action 2...")
        
        
        
class Command1(Command):
    def __init__(self, receiver: Receiver):
        self._receiver = receiver
    
    def execute(self):
        self._receiver.action1()
        
    def undo(self):
        print("Undoing Command 1...")
    
        
        
class Command2(Command):
    def __init__(self, receiver: Receiver):
        self._receiver = receiver
        
    def execute(self):
        self._receiver.action2()
        
    def undo(self):
        print("Undoing Command 2...")
        

if __name__ == "__main__":
    receiver = Receiver()
    command1 = Command1(receiver)
    command2 = Command2(receiver)
    invoker = Invoker()

    invoker.execute_command(command1)  # Output: Receiver executing action 1...
    invoker.execute_command(command2)  # Output: Receiver executing action 2...

    invoker.undo_last_command()  # Output: Undoing Command 2...
    invoker.undo_last_command()  # Output: Undoing Command 1...