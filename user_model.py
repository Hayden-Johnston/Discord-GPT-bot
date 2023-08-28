# author: Hayden Johnston
# date: 08/22/2023
# description: user model for GPT-3 chat memory

class User:
    """Define User object to maintain chat memory"""

    def __init__(self, id):
        self.depth = 2
        self.id = id
        self.memory = []

    def change_depth(self, depth):
        """Change user chat memory depth"""
        self.depth = depth
        return None
        
    def remember(self):
        """Remember user chat memory"""
        return self.memory
    
    def forget(self):
        """Forget user chat memory"""
        self.memory = []
        return None
    
    def update(self, content):
        """Update user chat memory"""
        if len(self.memory) >= self.depth:
            self.memory.pop(0)
            self.memory.append(content)
        else:
            self.memory.append(content)
        return None