import math
from Punto import Punto
from Linea import Linea


class Segmento:
    """Clase que representa un segmento entre dos puntos en el plano cartesiano 2D"""
    
    def __init__(self, p1: Punto = None, p2: Punto = None):
        """Inicializa un segmento con dos puntos"""
        self.p1 = p1 if p1 is not None else Punto(0, 0)
        self.p2 = p2 if p2 is not None else Punto(0, 0)
        self.longitud = self.Getlongitud()
        self.angulo = self.GetAngulo()
    
    def Getlongitud(self):
        """Calcula la longitud del segmento"""
        dx = self.p2.x - self.p1.x
        dy = self.p2.y - self.p1.y
        return math.sqrt(dx**2 + dy**2)
    
    def GetAngulo(self):
        """Calcula el ángulo del segmento respecto al eje X"""
        dx = self.p2.x - self.p1.x
        dy = self.p2.y - self.p1.y
        return math.atan2(dy, dx)
    
    def aLinea(self) -> Linea:
        """Convierte el segmento a una línea usando la ecuación:
        (y1 - y2)x + (x2 - x1)y + (x1*y2 - y1*x2) = 0
        donde A = (y1 - y2), B = (x2 - x1), C = (x1*y2 - y1*x2)
        """
        A = self.p1.y - self.p2.y
        B = self.p2.x - self.p1.x
        C = self.p1.x * self.p2.y - self.p1.y * self.p2.x
        
        return Linea(A, B, C)
    
    def interseccion(self, segmento: 'Segmento') -> Punto:
        self_linea = self.aLinea()
        otro_linea = segmento.aLinea()
        
        if self_linea.comparar(otro_linea):  # Son la misma línea
            puntos = [
                (0, self.p1),
                (self.longitud, self.p2),
                (self.p1.distancia(segmento.p1), segmento.p1),
                (self.p1.distancia(segmento.p2), segmento.p2)
            ]
            
            puntos.sort(key=lambda x: x[0])
            punto_inicio = puntos[1][1]
            punto_fin = puntos[2][1]
            
            tolerancia = 1e-10
            if punto_inicio.distancia(punto_fin) > tolerancia:
                # Retornar una lista con los dos puntos de superposición
                return [punto_inicio, punto_fin]
            else:
                return punto_inicio
        
        interseccion_linea = self_linea.interseccion(otro_linea)
        
        if interseccion_linea is None:
            return None
        
        # Verificar si la intersección está dentro de ambos segmentos
        en_segmento1 = (
            min(self.p1.x, self.p2.x) <= interseccion_linea.x <= max(self.p1.x, self.p2.x) and
            min(self.p1.y, self.p2.y) <= interseccion_linea.y <= max(self.p1.y, self.p2.y)
        )
        
        en_segmento2 = (
            min(segmento.p1.x, segmento.p2.x) <= interseccion_linea.x <= max(segmento.p1.x, segmento.p2.x) and
            min(segmento.p1.y, segmento.p2.y) <= interseccion_linea.y <= max(segmento.p1.y, segmento.p2.y)
        )
        
        if en_segmento1 and en_segmento2:
            return interseccion_linea
        else:
            return None
    
    def distancia(self, punto: Punto) -> float:
        """Calcula la distancia mínima de un punto al segmento"""
        self_linea = self.aLinea()
        
        # Línea perpendicular que pasa por el punto
        Ap = -self_linea.B
        Bp = self_linea.A
        Cp = self_linea.B * punto.x - self_linea.A * punto.y
        linea2 = Linea(Ap, Bp, Cp)
        interseccion_punto = self_linea.interseccion(linea2)
        
        if interseccion_punto is None:
            # Las líneas son paralelas (caso muy raro)
            return min(punto.distancia(self.p1), punto.distancia(self.p2))
        
        # Verificar si la intersección está dentro del segmento
        en_segmento = (
            min(self.p1.x, self.p2.x) - 1e-10 <= interseccion_punto.x <= max(self.p1.x, self.p2.x) + 1e-10 and
            min(self.p1.y, self.p2.y) - 1e-10 <= interseccion_punto.y <= max(self.p1.y, self.p2.y) + 1e-10
        )
        
        if en_segmento:
            return punto.distancia(interseccion_punto)
        else:
            return min(punto.distancia(self.p1), punto.distancia(self.p2))
    
    def distanciaPunto(self, punto: Punto) -> Punto:
        """Retorna el punto del segmento más cercano al punto dado"""
        self_linea = self.aLinea()
        
        # Línea perpendicular que pasa por el punto
        Ap = -self_linea.B
        Bp = self_linea.A
        Cp = self_linea.B * punto.x - self_linea.A * punto.y
        linea2 = Linea(Ap, Bp, Cp)
        
        interseccion_punto = self_linea.interseccion(linea2)
        
        if interseccion_punto is None:
            # Las líneas son paralelas
            if punto.distancia(self.p1) < punto.distancia(self.p2):
                return self.p1
            else:
                return self.p2
        
        # Verificar si la intersección está dentro del segmento
        en_segmento = (
            min(self.p1.x, self.p2.x) - 1e-10 <= interseccion_punto.x <= max(self.p1.x, self.p2.x) + 1e-10 and
            min(self.p1.y, self.p2.y) - 1e-10 <= interseccion_punto.y <= max(self.p1.y, self.p2.y) + 1e-10
        )
        
        if en_segmento:
            return interseccion_punto
        else:
            # Devolver el extremo más cercano
            if punto.distancia(self.p1) < punto.distancia(self.p2):
                return self.p1
            else:
                return self.p2
    
    def contiene(self, punto: Punto) -> bool:
        tolerancia: float = 1e-10
        
        if punto == self.p1 or punto == self.p2:
            return False
    
        # Primero verifica que el punto esté dentro del bounding box del segmento
        en_rango_x = min(self.p1.x, self.p2.x) - tolerancia <= punto.x <= max(self.p1.x, self.p2.x) + tolerancia
        en_rango_y = min(self.p1.y, self.p2.y) - tolerancia <= punto.y <= max(self.p1.y, self.p2.y) + tolerancia
        
        if not (en_rango_x and en_rango_y):
            return False
        
        # Luego verifica que la distancia del punto al segmento sea prácticamente cero
        return self.distancia(punto) <= tolerancia
    
    def x_en(self, y: float) -> float:
        if abs(self.p1.y - self.p2.y) < 1e-12:  # segmento horizontal
            return (self.p1.x + self.p2.x) / 2.0
        t = (y - self.p1.y) / (self.p2.y - self.p1.y)
        return self.p1.x + t * (self.p2.x - self.p1.x)
    
    def __str__(self):
        """Representación en cadena del segmento"""
        return f"Segmento[{self.p1} -> {self.p2}] (L={self.longitud:.2f}, θ={math.degrees(self.angulo):.2f}°)"
    
    def __repr__(self):
        """Representación para debugging"""
        return f"Segmento(p1={repr(self.p1)}, p2={repr(self.p2)}, longitud={self.longitud:.2f}, angulo={self.angulo:.2f})"