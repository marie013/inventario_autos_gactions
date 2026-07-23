import json
import os

class Vehiculo():
    def __init__(self, marca, modelo, kilometraje, precio, patente):
        self.marca= marca
        self.kilometraje= kilometraje
        self.modelo = modelo
        self.precio = precio
        self.patente = patente

    def registrar_vehiculo():
        marca_auto=input("Ingrese la marca del auto")
        modelo_auto=input("Ingrese el modelo del auto")
        kilometraje_auto=input("Ingrese el kilometraje del auto")
        precio_auto=input("Ingrese el precio del auto")
        patente_auto=input("Ingrese la patente del auto")
        return Vehiculo(marca_auto, modelo_auto, kilometraje_auto, precio_auto, patente_auto)
    
    def dict_vehiculo(self):
        return {
            "marca": self.marca,
            "modelo": self.modelo,
            "kilometraje": self.kilometraje,
            "precio": self.precio,
            "patente": self.patente
        }
    
    @staticmethod
    def from_dict_vehiculo(datos):
        return Vehiculo(datos["marca"], datos["modelo"], datos["kilometraje"], datos["precio"], datos["patente"])
    def __str__(self):
        return  {self.marca}, {self.modelo}, {self.kilometraje}, {self.precio}, {self.patente}

class GestorVehiculo:
    def __init__(self, archivo_ruta="/POO/autos.json"):
        self.archivo = archivo_ruta 

    def guardar_vehiculo(self, vehiculos):
        guardar = [vehiculo.dict_vehiculo() for vehiculo in vehiculos]

        with open(self.archivo, "w", encoding="utf-8") as f:
            json.dump(guardar, f, indent=4, ensure_ascii=False)
        print("Datos guardados con éxito")

    # def cargar_vehiculo(self):
    #     if not os.path.exists(self.archivo):
    #         return []
    #     with open(self.archivo, "r", encoding="utf-8") as f:
    #         #guardar = json.load(f)

    #         objeto_vehiculo= Vehiculo.from_dict_vehiculo
    #         return objeto_vehiculo   
    
"""======= MENU =======
1. Agregar vehiculo
2. Buscar vehiculo por patente
3. Actualizar vehiculo
4. Ver listado de vehiculos
5. Salir""" 

# ruff check InventarioAutos.py
# mypy --strict InventarioAutos.py