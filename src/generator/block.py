

class Block:
    
    def __init__(self,value,is_pushable=False,is_movable=False):
        self.value = value
        self.push = is_pushable
        self.move = is_movable
        
    def __repr__(self):
        return self.value