import pymysql as psql
from Modelo.cliente import Cliente
from Modelo.chofer import Chofer
from Modelo.vehiculo import Vehiculo
import subprocess

class BaseDatos():
    def __init__(self):
         self.sql = ''
         self.__conn = None
         self.activarServidor()
         self.conexionSql()

    def activarServidor(self):
        # Comando para iniciar el servicio MySQL en Windows
        comando = "net start mysql"
        # Ejecutar el comando
        subprocess.run(comando, shell=True, capture_output=True, text=True)

    def conexionSql(self):
        try:
            self.__conn = psql.connect(
                host='localhost',
                user='root',
                port=3306,
                password='12345',
                charset='utf8'
            )
            self.crearBD()
            self.crearTablas()
        except psql.MySQLError as ex:
            print(ex)
            
    def crearBD(self):
        try:
            with self.__conn.cursor() as cursor:
                self.sql = 'create database if not exists transporte'
                cursor.execute(self.sql)
                self.__conn.commit()
                print('base de datos creada correctamente')
                self.crearTablas()
        except psql.MySQLError as ex:
                print(ex)

    def crearTablas(self):
        try:
            self.__conn.select_db('transporte')
            with self.__conn.cursor() as cursor:
                self.sql = '''
                    create table if not exists chofer(
                    Id_Chofer int Primary key auto_increment not null,
                    Cedula varchar(25) not null,
                    Nombres varchar(25) not null,
                    Apellidos varchar(25) not null
                );'''
                cursor.execute(self.sql)
                self.sql='''
                    create table if not exists vehiculo(
                        Id_Vehiculo INT PRIMARY KEY AUTO_INCREMENT not null,
                        Cap_Pasajeros int not null,
                        Marca varchar(25) not null,
                        Chofer_Id int not null,
                        constraint fk_IdChofer foreign key(Chofer_Id)
                        references chofer(Id_Chofer) 
                    );'''
                cursor.execute(self.sql)
                self.sql='''
                    create table if not exists cliente(
                        Id_Cliente int Primary key auto_increment not null,
                        Cedula varchar(25) not null,
                        Nombres varchar(25) not null,
                        Apellidos varchar(25) not null
                    );'''
                cursor.execute(self.sql)
                self.sql = '''
                    create table if not exists viaje(
                        Id_Viaje int Primary key auto_increment not null,
                        Lugar_Destino varchar(25) not null,
                        Hora_Llegada varchar(25) not null,
                        Hora_Salida varchar(25) not null,
                        Cliente_Id int not null,
                        constraint fk_IDcliente foreign key(Cliente_Id)
                        references cliente(Id_Cliente),
                        Vehiculo_Id int not null,
                        constraint fk_IdVehiculo foreign key(Vehiculo_Id)
                        references vehiculo(Id_Vehiculo)
                    );'''
                cursor.execute(self.sql)
                self.__conn.commit()
                print('Tablas creadas correctamente')
        except psql.MySQLError as ex:
            print(ex)

    def ingresar(self, entidad:object):
        try:
            with self.__conn.cursor() as cursor:
                if isinstance(entidad,Chofer):
                        self.sql = f''' 
                            insert into chofer(Cedula, Nombres, Apellidos) 
                            values (
                                '{entidad.Cedula}', 
                                '{entidad.Nombres}', 
                                '{entidad.Apellidos}'
                                );
                        '''
                elif isinstance(entidad, Vehiculo):
                        self.sql = f''' 
                            insert into vehiculo(Cap_Pasajeros, Marca, Chofer_Id) 
                            values (
                                '{entidad.CapPasajeros}', 
                                '{entidad.Marca}', 
                                '{entidad.ChoferId}'
                                );
                        '''
                elif isinstance(entidad, Cliente):
                        self.sql = f''' 
                            insert into cliente(Cedula, Nombres, Apellidos) 
                            values (
                                '{entidad.Cedula}',
                                '{entidad.Nombres}', 
                                '{entidad.Apellidos}'
                                );
                        '''
                else:
                        self.sql = f''' 
                            insert into viaje(Lugar_Destino, Hora_Llegada, Hora_Salida, Cliente_Id, Vehiculo_Id ) 
                            values (
                                '{entidad.LugarDestino}',
                                '{entidad.HoraLlegada}',
                                '{entidad.HoraSalida}',
                                '{entidad.ClienteId}',
                                '{entidad.VehiculoId}'
                                );
                            '''
                cursor.execute(self.sql)
                self.__conn.commit()
                print("Registro hecho correctamente.")

        except psql.MySQLError as ex:
            print(ex)  
            print('Registro') 
    
    def modificar(self, entidad:object):
        try:
            with self.__conn.cursor() as cursor:
                if isinstance(entidad,Chofer):
                        self.sql = f''' 
                            update chofer 
                            set Cedula = '{entidad.Cedula}', 
                                Nombres = '{entidad.Nombres}', 
                                Apellidos = '{entidad.Apellidos}'
                            where Id_Chofer = '{entidad.IdChofer}';
                        '''
                elif isinstance(entidad, Vehiculo):
                        self.sql = f''' 
                            update vehiculo 
                            set Cap_Pasajeros = '{entidad.CapPasajeros}',
                                Marca = '{entidad.Marca}',
                                Chofer_Id = '{entidad.ChoferId}'
                            where Id_Vehiculo = '{entidad.IdVehiculo}';
                        '''
                elif isinstance(entidad, Cliente):
                        self.sql = f''' 
                            update cliente 
                            set Cedula = '{entidad.Cedula}', 
                                Nombres = '{entidad.Nombres}', 
                                Apellidos = '{entidad.Apellidos}' 
                            where Id_Cliente = '{entidad.IdCliente}';
                        '''
                else:
                        self.sql = f''' 
                            update viaje
                            set Lugar_Destino = '{entidad.LugarDestino}', 
                                Hora_Llegada = '{entidad.HoraLlegada}', 
                                Hora_Salida = '{entidad.HoraSalida}', 
                                Cliente_Id = '{entidad.ClienteId}', 
                                Vehiculo_Id = '{entidad.VehiculoId}'
                            where Id_Viaje = '{entidad.IdViaje}';
                            '''
                cursor.execute(self.sql)
                self.__conn.commit()
                print("Registro actualizado correctamente.")
        except psql.MySQLError as e:
            print(e)
            print('modificar')
            self.__conn.rollback()

    def buscarTodo(self, entidad_numero):
        try:
            with self.__conn.cursor() as cursor:
                if entidad_numero == 0:
                    self.sql = 'select * from viaje'
                elif entidad_numero == 1:
                    self.sql = 'select * from vehiculo'
                elif entidad_numero == 2:
                    self.sql = 'select * from chofer;'
                else:
                    self.sql = 'select * from cliente'
                cursor.execute(self.sql)
                datos = cursor.fetchall()
                print("Busqueda hecha correctamente.")
                return datos
        except psql.MySQLError as e:
            print(e)
            print('Buscar Todo')
            return []
        
    def buscarId(self, entidad_numero, id):
        try:
            with self.__conn.cursor() as cursor:
                if entidad_numero == 0:
                    self.sql = f'select * from viaje where Id_Viaje = {id};'
                elif entidad_numero == 1:
                    self.sql = f'select * from vehiculo where Id_Vehiculo = {id};'
                elif entidad_numero == 2:
                    self.sql = f'select * from chofer where Id_Chofer = {id};'
                else:
                    self.sql = f'select * from cliente where Id_Cliente = {id};'
                cursor.execute(self.sql)
                datos = cursor.fetchall()
                datos = [dato for x in datos for dato in x]
                print("Busqueda hecha correctamente.")
                return datos
        except psql.MySQLError as e:
            return []
        
    def buscarDependencia(self, entidad, id):
        try:
            with self.__conn.cursor() as cursor:
                if entidad == 0:
                    self.sql = f'select Cliente_Id from viaje where Cliente_Id = {id} and Id_Viaje<>0;'
                elif entidad == 1:
                    self.sql = f'select Vehiculo_Id from viaje where Vehiculo_Id = {id} and Id_Viaje<>0;'
                elif entidad == 2:
                    self.sql = f'select Chofer_Id from vehiculo where Chofer_Id = {id} and Id_Vehiculo<>0;'
                else:
                    self.sql = f'select * from cliente where Id_Cliente = {id};'
                cursor.execute(self.sql)
                datos = cursor.fetchall()
                datos = [dato for x in datos for dato in x]
                print("Busqueda hecha correctamente.")
                return datos
        except psql.MySQLError as e:
            print(e)
            print('Buscar Deoebdeciuas')
            return []
    
    def eliminar(self, id,entidad):
        try:
            with self.__conn.cursor() as cursor:
                if entidad == 0:
                        self.sql = f'delete from chofer where Id_Chofer = {id};'
                elif entidad == 1:
                        self.sql = f'delete from vehiculo where Id_Vehiculo = {id};'
                elif entidad == 2:
                        self.sql = f'delete from cliente where Id_Cliente = {id};'
                else:
                        self.sql = f'delete from viaje where Id_Viaje = {id};'
                cursor.execute(self.sql)
                self.__conn.commit()
                print("eliminacion hecha correctamente.")
        except psql.MySQLError as e:
            print(e)
            print('Elimianr')