import random

class VehiculoAutomotor:

    def __init__(self, color, modelo, numcyl, ruedas, transmision):
        self.color = color
        self.modelo = modelo
        self.numCyl = numcyl
        self.numRuedas = ruedas
        self.transmision = transmision

    def encender(self):
        print('Encender')
    
    def acelerar(self):
        print('Acelerar')
    
    def frenar(self):
        print('Frenar')

    def sacarClutch(self):
        print('sacar clutch')

    def meterClutch(self):
        print('meter clutch')

class Moto(VehiculoAutomotor):

    def __init__(self,  color, modelo, numcyl, ruedas, transmision):
        super().__init__(color, modelo, numcyl, ruedas, transmision)
        self._manillarDerecha = False
        self._manillarIzquierda = False 

    def bajarPataLateral(self):
        print('Estacionarse')
    
    def subirPataLateral(self):
        print('No estacionado')

class Automovil(VehiculoAutomotor):

    def __init__(self,  color, modelo, numcyl, ruedas, transmision):
        super().__init__(color, modelo, numcyl, ruedas, transmision)
        self._volantiarDerecha = False
        self._volantiarIzquierda = False

    def subirFrenoDeMano(self):
        print('Estacionarse')

    def bajarFrenoDeMano(self):
        print('No Estacionado')

if __name__ == "__main__":

    semaforo = False # 1:verde, 2:amarillo, 3:rojo
    Ninja = Moto('Azul','2024','1','2','standard')
    BMW = Moto('Negra','2015','1','2', 'standard')
    Cupra = Automovil('Gris', '2024', '6', '4', 'standard')

    Ninja.encender()
    BMW.encender()
    Cupra.encender()

    Ninja.subirPataLateral()
    BMW.subirPataLateral()
    Cupra.bajarFrenoDeMano()

    vehiculos = [Ninja, BMW, Cupra]

    num = random.randint(0, 9)

    if num % 2 == 0:
        semaforo = True
        print('Arranquen')
    else:
        print('esperen arranque')
    
    if semaforo:
        for i in range(len(vehiculos)):
            vehiculos[i].acelerar()
            
        





