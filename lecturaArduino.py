from datetime import datetime

import mongo
import serial
import time

from Sensor import Sensor
from datosSensor import DatosSensor
import os


interacciondb = mongo.MongoConexion("mongodb://localhost:27017", "sistemaSensores", "Sensores")

class DatoSensor():
    def __init__(self):
        self.lista = DatosSensor()
        self.lista.toObjects()


    def cls(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def leerSensor(self):
        ser = serial.Serial('COM5', 9600)  # Reemplaza 'COM3' con el nombre del puerto serial del Arduino

        i = 0
        print("-" * 20 + "leyendo datos" + "-" * 20)

        time.sleep(1)
        cadena = ser.readline()
        if cadena:
                #time.sleep(2)
                now = datetime.now()
                print(cadena)
                print(now)
                dts=DatosSensor()
                dts.datos=cadena
                dts.fecha=now
        return dts




    def menuSensor(self):
        a = 10
        while a != 0:
            self.cls()
            print("\n\n" + "-" * 10 + "Menu lectura de Sensor" + "-" * 10)
            print("1) Leer Sensor\n0)salir")

            a = input("Selecciona una opción: ")
            if (a == '1'):
                p = self.leerSensor()

                self.lista.add(p)


            elif (a == '0'):
                break
            else:
                print("La opcion no es correcta vuelve a seleccionar da enter para continuar.....")
                input()





