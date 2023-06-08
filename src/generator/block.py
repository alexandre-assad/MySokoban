

class Block:
    
    def __init__(self,value,is_pushable=False,is_movable=False):
        self.value = value
        self.is_pushable = is_pushable
        self.is_movable = is_movable