class Rule:
    
    def __init__(self, reglas: dict):
        self.reglas = reglas if reglas is not None else {}
    
    def check(self, current: str) -> str:
        return self.reglas.get(current, current)
    
    def agregar_regla(self, simbolo: str, reemplazo: str):
        self.reglas[simbolo] = reemplazo
    
    def __str__(self):
        lineas = [f"{simbolo} -> {reemplazo}" for simbolo, reemplazo in self.reglas.items()]
        return "\n".join(lineas)
    
    def __repr__(self):
        return f"Rule(reglas={self.reglas})"