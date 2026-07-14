import math
import matplotlib.pyplot as plt
from Punto import Punto
from Segmento import Segmento
from Graficador import graficar_segmento, configurar_grafico

from Rule import Rule

def generar_l_system(n : int, initialLetter : str, rule1 : Rule):
    finalString = initialLetter
    for i in range(n):
        newString = ""
        for j in range(len(finalString)):
            char = finalString[j]
            char = rule1.check(char)
            newString += char
        finalString = newString
    return finalString

def turtle_segments(instructions : str, angle : float, length : int):
    position_stack = []
    segments = []
    position = Punto(0, 0)
    direction = math.pi / 2
    
    for simbolo in instructions:
        if simbolo == "F": #AVANZA
            new_x = position.x + (length * math.cos(direction))
            new_y = position.y + (length * math.sin(direction))
            new_position = Punto(new_x, new_y)
            
            segments.append(Segmento(position, new_position))
            position = new_position
            
        if simbolo == "+":
            direction += angle
            
        if simbolo == "-":
            direction -= angle
            
        if simbolo == "[":
            position_stack.append((position, direction))
            
        if simbolo == "]":
            position, direction = position_stack.pop()

    return segments

rule1 = Rule("F", "FF+[+F-F-F]-[-F+F+F]")
instructions = generar_l_system(3, "F", rule1)

angle = math.radians(25)
lenght = 1
segmentos = turtle_segments(instructions, angle, lenght)

fig, ax = plt.subplots(figsize=(8, 8))
for seg in segmentos:
    graficar_segmento(seg, ax=ax, color='green', linewidth=1)
    
configurar_grafico(ax, title='Árbol L-System')
plt.show()

