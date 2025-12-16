import pandas as pd
import matplotlib.pyplot as plt
import os
from typing import Dict, List

class Articulo:
    def __init__(self, codigo, nombre, stock, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.stock = stock
        self.precio = precio
    
    def agregar_stock(self, cantidad):
        self.stock += cantidad
    
    def retirar_stock(self, cantidad):
        self.stock -= cantidad

    def __repr__(self):
        return f"{self.codigo} - {self.nombre} | Stock: {self.stock} | Precio: {self.precio}"

#Creo que esto podría ser mas facil si solo lo habrimos desde excel con pandas. Pero probemos:
class Inventario:
    def __init__(self):
        self.articulos: Dict[str, Articulo] = {}
    
    def agregar_articulo(self, articulo:Articulo):
        if articulo.codigo in self.articulos:
            raise ValueError('El articulo ya existe')
        self.articulos[articulo.codigo] == articulo
    
    def listar(self):
        return [str(a) for a in self.articulos.values()]

class SistenaInventario:
    def __init__(self):
        self.inventario = Inventario

    def mostrarMenu(self):
        pass

def menu_principal():

    menu_abierto = True
    while menu_abierto:
    
        print(
            "1. Mostrar Inventario\n" \
            "2. Buscar producto\n" \
            "3. Agregar producto\n" \
            "4. Editar información de un producto\n" \
            "5. Eliminar producto\n" \
            "6. Generar reporte\n" \
            "7. Salir\n"
        )

        opcion = input("Introduce la opción:" )
        limpiar()
        match opcion:
            case '1':
                mostrar_inventario()
                menu_abierto = False
            case '2':
                buscar_producto()
                menu_abierto = False

            case '3':
                agregar_producto()
                menu_abierto = False

            case '4':
                editar_info()
                menu_abierto = False
            
            case '5':
                eliminar_producto()
                menu_abierto = False

            case '6':
                generar_reporte()
                menu_abierto = False

            case '7':
                print('Adios')
                menu_abierto = False
            case _:
                print("Vuelva a introducir una opción")

def mostrar_inventario():
    print("Entraste al inventario")
def buscar_producto():
    print("Entraste a buscar un producto")
def agregar_producto():
    print("Entraste a agregar un producto")
def eliminar_producto():
    print("Eliminar producto")
def editar_info():
    print("Entraste a editar")
def generar_reporte():
    print("Ten tu reporte")
    
def limpiar():
    os.system("cls" if os.name == "nt" else "clear")

menu_principal()

#Cambiandonos al repositorio del compańero