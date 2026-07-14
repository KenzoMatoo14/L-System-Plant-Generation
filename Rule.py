import math

class Rule:
    def __init__(self, axiom1: str, axiom2: str):
        self.axiom1 = axiom1 if axiom1 is not None else "X"
        self.axiom2 = axiom2 if axiom2 is not None else "X"
        
    def check(self, current):
        
        NewAxiom = ""
        if current == self.axiom1:
            NewAxiom += self.axiom2
        else:
            NewAxiom += current
            
        return NewAxiom
            
