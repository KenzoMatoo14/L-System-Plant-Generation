from Punto import Punto


class Linea:
    """Clase que representa una línea recta en el plano cartesiano 2D
    
    La línea se representa en forma general: Ax + By + C = 0
    """
    
    def __init__(self, A: float = 0.0, B: float = 0.0, C: float = 0.0):
        self.A = float(A)
        self.B = float(B)
        self.C = float(C)
    
    def distancia(self, punto: Punto) -> float:
        """Calcula la distancia perpendicular de un punto a la línea"""
        Ap = -self.B
        Bp = self.A
        Cp = self.B * punto.x - self.A * punto.y
        linea2 = Linea(Ap, Bp, Cp)
        interseccion_punto = self.interseccion(linea2)
        distancia = punto.distancia(interseccion_punto)
        
        return distancia
    
    def distanciaPunto(self, punto: Punto) -> Punto:
        """Retorna el punto de la línea más cercano al punto dado"""
        Ap = -self.B
        Bp = self.A
        Cp = self.B * punto.x - self.A * punto.y
        linea2 = Linea(Ap, Bp, Cp)
        interseccion_punto = self.interseccion(linea2)
        
        return interseccion_punto
    
    def interseccion(self, linea2: 'Linea') -> Punto:
        """Calcula el punto de intersección con otra línea
        
        Retorna None si las líneas son paralelas
        """
        det = self.A * linea2.B - linea2.A * self.B 
        
        if det == 0:  # Son paralelas
            return None
        else:
            detX = -self.C * linea2.B + linea2.C * self.B
            detY = -self.A * linea2.C + linea2.A * self.C
            
            dx = detX / det
            dy = detY / det
            
            return Punto(dx, dy)
    
    def comparar(self, linea2: 'Linea') -> bool:
        tolerancia = 1e-10
        
        # Casos especiales cuando algún coeficiente es 0
        # Si A y A2 son ambos 0 (línea horizontal)
        if abs(self.A) < tolerancia and abs(linea2.A) < tolerancia:
            if abs(self.B) < tolerancia or abs(linea2.B) < tolerancia:
                return False
            # Ambas son horizontales, verificar si C/B es igual
            return abs(self.C / self.B - linea2.C / linea2.B) < tolerancia
        
        # Si B y B2 son ambos 0 (línea vertical)
        if abs(self.B) < tolerancia and abs(linea2.B) < tolerancia:
            if abs(self.A) < tolerancia or abs(linea2.A) < tolerancia:
                return False
            # Ambas son verticales, verificar si C/A es igual
            return abs(self.C / self.A - linea2.C / linea2.A) < tolerancia
        
        # Caso general: verificar proporcionalidad
        # Encontrar un coeficiente no nulo para calcular la razón
        if abs(self.A) > tolerancia and abs(linea2.A) > tolerancia:
            ratio = self.A / linea2.A
        elif abs(self.B) > tolerancia and abs(linea2.B) > tolerancia:
            ratio = self.B / linea2.B
        else:
            return False
        
        # Verificar que todos los coeficientes tengan la misma razón
        if abs(self.A) > tolerancia and abs(linea2.A) > tolerancia:
            if abs(self.A / linea2.A - ratio) > tolerancia:
                return False
        elif abs(self.A) > tolerancia or abs(linea2.A) > tolerancia:
            return False
        
        if abs(self.B) > tolerancia and abs(linea2.B) > tolerancia:
            if abs(self.B / linea2.B - ratio) > tolerancia:
                return False
        elif abs(self.B) > tolerancia or abs(linea2.B) > tolerancia:
            return False
        
        if abs(self.C) > tolerancia and abs(linea2.C) > tolerancia:
            if abs(self.C / linea2.C - ratio) > tolerancia:
                return False
        elif abs(self.C) > tolerancia or abs(linea2.C) > tolerancia:
            return False
        
        return True
    
    def __str__(self):
        """Representación en cadena de la línea"""
        return f"{self.A}x + {self.B}y + {self.C} = 0"
    
    def __repr__(self):
        """Representación para debugging"""
        return f"Linea(A={self.A}, B={self.B}, C={self.C})"