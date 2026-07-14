import math

"""Clase que representa un punto en el plano cartesiano 2D"""
class Punto:
    def __init__(self, x: float = 0.0, y: float = 0.0):
        self.x = float(x)
        self.y = float(y)
    
    def trasladar(self, dx: float, dy: float):
        self.x += dx
        self.y += dy
    
    def rotar(self, angulo: float, origen=None):
        if origen is None:
            origen = Punto(0, 0)
        
        # Trasladar al origen
        x_temp = self.x - origen.x
        y_temp = self.y - origen.y
        
        # Aplicar rotación
        cos_a = math.cos(angulo)
        sin_a = math.sin(angulo)
        
        x_rot = x_temp * cos_a - y_temp * sin_a
        y_rot = x_temp * sin_a + y_temp * cos_a
        
        # Crear y retornar nuevo punto
        return Punto(x_rot + origen.x, y_rot + origen.y)
    
    def a_polar(self) -> tuple:
        r = math.sqrt(self.x**2 + self.y**2)
        theta = math.atan2(self.y, self.x)
        return (r, theta)
    
    def distancia(self, otro) -> float:
        distancia = math.sqrt((self.x - otro.x)**2 + (self.y - otro.y)**2)
        
        return distancia
    
    def comparar(self, otro) -> dict:
        if not isinstance(otro, Punto):
            raise TypeError("Se debe comparar con otro objeto Punto")
        
        distancia = self.distancia(otro)
        son_iguales = math.isclose(self.x, otro.x) and math.isclose(self.y, otro.y)
        
        return {
            'son_iguales': son_iguales,
            'distancia': distancia,
            'dx': otro.x - self.x,
            'dy': otro.y - self.y
        }
    
    def __str__(self):
        """Representación en cadena del punto"""
        return f"Punto({self.x:.2f}, {self.y:.2f})"
    
    def __repr__(self):
        """Representación para debugging"""
        return f"Punto(x={self.x}, y={self.y})"
    
    def __lt__(self, other):
        if self.y != other.y:
            return self.y > other.y  # mayor y primero
        return self.x < other.x     # desempate por x
    
    def __eq__(self, other):
        if not isinstance(other, Punto):
            return False
        return math.isclose(self.x, other.x) and math.isclose(self.y, other.y)

    def __hash__(self):
        # Redondear para que puntos muy cercanos tengan el mismo hash
        return hash((round(self.x, 9), round(self.y, 9)))