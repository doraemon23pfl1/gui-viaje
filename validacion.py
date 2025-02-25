import re
from baseDatos import BaseDatos
from datetime import datetime


class Validacion():
    def esNumero(self, texto):
        try:
            float(texto)
            return True
        except ValueError:
            return False

    def verificarHora(self, texto):
        try:
            # Convertir la cadena a un objeto datetime
            hora = datetime.strptime(texto, "%H:%M").time()
            return True
        except ValueError:
            return False


    def noTieneNumero(self, texto):
        # Patrón para verificar que la cadena no contenga números
        patron = re.compile(r'^[^\d]+$')
        if patron.match(texto):
            return True
        else:
            return False
        
    def noEstaBlanco(self,texto):
        if texto.strip():
            return True
        else:
            return False

    def noEstaVacio(self,texto):
        if texto:
            return True
        else:
            return False

    def existeChofer(self, id_Chofer):
        db = BaseDatos()
        dato = db.buscarId(2, id_Chofer)
        if dato:
            return True
        else:
            return False

    def existeCliente(self, id_Cliente):
        db = BaseDatos()
        dato = db.buscarId(3, id_Cliente)
        if dato:
            return True
        else:
            return False
    
    def existeVehiculo(self, id_vehiculo):
        db = BaseDatos()
        dato = db.buscarId(1, id_vehiculo)
        if dato:
            return True
        else:
            return False
    
    def existeViaje(self, id_viaje):
        db = BaseDatos()
        dato = db.buscarId(0, id_viaje)
        if dato:
            return True
        else:
            return False
        
    def verificar_info(self, l):
        if l:
            return 1
        else:
            return 0
    
    def verificarDependenciaChoferVehiculo(self, entidad, id_chofer):
        db = BaseDatos()
        datos = db.buscarDependencia(entidad, id_chofer)
        print(datos)
        if datos:
            return True
        else:
            return False
    
    def verificarDependenciaClienteViaje(self, entidad, Id_Cliente):
        db = BaseDatos()
        datos = db.buscarDependencia(entidad, Id_Cliente)
        print(datos)
        if datos:
            return True
        else:
            return False

    def verificarDependenciaVehiculoViaje(self, entidad, Vehiculo_id):
        db = BaseDatos()
        datos = db.buscarDependencia(entidad, Vehiculo_id)
        print(datos)
        if datos:
            return True
        else:
            return False

v = Validacion()
print(v.verificarDependenciaVehiculoViaje(1,2))
print(v.verificarDependenciaClienteViaje(0,1))
print(v.verificarHora('23:12'))