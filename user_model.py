# author: Hayden Johnston
# date: 08/22/2023
# description: user model for GPT-3 chat memory

class User:
    """Define User object to maintain chat memory"""

    def __init__(self, id, memory):
        self.depth = 2
        self.id = id
        self.memory = memory
        