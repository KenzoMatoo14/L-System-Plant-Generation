import numpy as np
import matplotlib.pyplot as plt
from Punto import Punto
from Linea import Linea
from Segmento import Segmento


def graficar_punto(punto, ax=None, color='red', marker='o', zorder=1, size=100, label=None):
    """Grafica un punto en el plano cartesiano"""
    if ax is None:
        fig, ax = plt.subplots(figsize=(8, 8))
    
    ax.scatter(punto.x, punto.y, c=color, marker=marker, s=size, label=label, zorder=zorder)
    ax.text(punto.x + 0.2, punto.y + 0.2, f'({punto.x:.2f}, {punto.y:.2f})', 
            fontsize=9, ha='left')
    
    return ax


def graficar_segmento(segmento, ax=None, color='blue', zorder=1, linewidth=2, label=None):
    """Grafica un segmento en el plano cartesiano"""
    if ax is None:
        fig, ax = plt.subplots(figsize=(8, 8))
    
    x_vals = [segmento.p1.x, segmento.p2.x]
    y_vals = [segmento.p1.y, segmento.p2.y]
    
    ax.plot(x_vals, y_vals, color=color, linewidth=linewidth, label=label, zorder=zorder)
    
    # Marcar los puntos extremos
    ax.scatter([segmento.p1.x, segmento.p2.x], 
              [segmento.p1.y, segmento.p2.y], 
              c=color, marker='o', s=50, zorder=zorder)
    
    return ax


def graficar_linea(linea, ax=None, color='green', linewidth=1.5, 
                   linestyle='--', label=None, xlim=None, ylim=None):
    """Grafica una línea en el plano cartesiano
    
    La línea se extiende dentro de los límites especificados o del gráfico actual
    """
    if ax is None:
        fig, ax = plt.subplots(figsize=(8, 8))
        if xlim is None:
            xlim = (-10, 10)
        if ylim is None:
            ylim = (-10, 10)
    else:
        if xlim is None:
            xlim = ax.get_xlim()
        if ylim is None:
            ylim = ax.get_ylim()
    
    # Ax + By + C = 0
    # Si B != 0: y = -(A*x + C) / B
    # Si B == 0: x = -C / A (línea vertical)
    
    if abs(linea.B) > 1e-10:  # Línea no vertical
        x_vals = np.array(xlim)
        y_vals = -(linea.A * x_vals + linea.C) / linea.B
        ax.plot(x_vals, y_vals, color=color, linewidth=linewidth, 
               linestyle=linestyle, label=label, zorder=2)
    else:  # Línea vertical (B = 0)
        if abs(linea.A) > 1e-10:
            x_val = -linea.C / linea.A
            y_vals = np.array(ylim)
            ax.plot([x_val, x_val], y_vals, color=color, linewidth=linewidth,
                   linestyle=linestyle, label=label, zorder=2)
    
    return ax


def configurar_grafico(ax, title='Gráfico de Geometría', grid=True, 
                       equal_aspect=True, xlim=None, ylim=None):
    """Configura los aspectos visuales del gráfico"""
    ax.set_title(title, fontsize=14, fontweight='bold')
    ax.set_xlabel('X', fontsize=12)
    ax.set_ylabel('Y', fontsize=12)
    
    if grid:
        ax.grid(True, alpha=0.3, linestyle=':', linewidth=0.5)
    
    if equal_aspect:
        ax.set_aspect('equal', adjustable='box')
    
    if xlim:
        ax.set_xlim(xlim)
    if ylim:
        ax.set_ylim(ylim)
    
    # Añadir ejes cartesianos
    ax.axhline(y=0, color='k', linewidth=0.5, alpha=0.5)
    ax.axvline(x=0, color='k', linewidth=0.5, alpha=0.5)
    
    # Mostrar leyenda si hay elementos etiquetados
    handles, labels = ax.get_legend_handles_labels()
    if labels:
        ax.legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize=9, framealpha=0.9)