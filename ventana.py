from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QMessageBox
from Modelo.cliente import Cliente
from Modelo.chofer import Chofer
from Modelo.vehiculo import Vehiculo
from Modelo.viaje import Viaje
from validacion import Validacion
from baseDatos import BaseDatos

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Ventana.ui',self) #Cargar archivo .ui
        self.stacked_pages = self.pages  # Asigna el QStackedWidget a un atributo
        self.stacked_pages_Datos = self.pages_Datos  
        self.stacked_pages_Registrar = self.pages_Registrar  
        self.stacked_pages_Modificar = self.pages_Modificar 
        self.stacked_pages_Buscar = self.pages_Buscar 
        self.stacked_pages_Eliminar = self.pages_Eliminar

        self.botonBuscar = self.Boton_Buscar  # Asigna el botón a un atributo
        self.botonEliminar = self.Boton_Eliminar
        self.botonActualizar = self.Boton_Refrescar_Datos
        self.botonDatos = self.Boton_BaseDatos
        self.botonModificar = self.Boton_Modificar
        self.botonRegistrar = self.Boton_Registrar
        self.botonRgViaje = self.Boton_Registrar_Viaje
        self.botonRgVehiculo = self.Boton_Registrar_Vehiculo
        self.botonRgChofer = self.Boton_Registrar_Chofer
        self.botonRgCliente = self.Boton_Registrar_Cliente
        self.botonMdViaje = self.Boton_Viaje_Modificar
        self.botonMdVehiculo = self.Boton_Vehiculo_Modificar
        self.botonMdChofer = self.Boton_Chofer_Modificar
        self.botonMdCliente = self.Boton_Cliente_Modificar
        self.botonBcChofer = self.Boton_ChoferBuscar_Buscar
        self.botonBcCliente = self.Boton_ClienteBuscar_Buscar
        self.botonBcViaje = self.Boton_ViajeBuscar_Buscar
        self.botonBcVehiculo = self.Boton_VehiculoBuscar_Buscar
        self.botonBcChoferDel = self.Boton_IdChoferBuscar_Eliminar
        self.botonBcClienteDel = self.Boton_IdClienteBuscar_Eliminar
        self.botonBcViajeDel = self.Boton_IdViajeBuscar_Eliminar
        self.botonBcVehiculoDel = self.Boton_IdVehiculoBuscar_Eliminar
        self.botonDelChofer = self.Boton_Chofer_Eliminar
        self.botonDelCliente = self.Boton_Cliente_Eliminar
        self.botonDelViaje = self.Boton_Viaje_Eliminar
        self.botonDelVehiculo = self.Boton_Vehiculo_Eliminar

        self.tablaChoferDatos = self.tableWidget_Chofer_Datos # Asigna la tabla a un atributo
        self.tablaClienteDatos = self.tableWidget_Cliente_Datos 
        self.tablaViajeDatos = self.tableWidget_Viaje_Datos 
        self.tablaVehiculoDatos = self.tableWidget_Vehiculo_Datos
        self.tablaClienteDel= self.tableWidget_Cliente_Eliminar
        self.tablaViajeDel = self.tableWidget_Viaje_Eliminar
        self.tablaVehiculoDel = self.tableWidget_Vehiculo_Eliminar 
        self.tablaChoferDel = self.tableWidget_Chofer_Eliminar 

        self.leHoraLlegadaRg = self.lineEdit_HoraLlegada_Registrar # Asigna valor de line a un atributo
        self.leHoraSalidaRg = self.lineEdit_HoraSalida_Registrar
        self.leLugarDestinoRg = self.lineEdit_LugarDestino_Registrar
        self.leViajeIdClienteRg = self.lineEdit_ViajeClienteId_Registrar
        self.leViajeIdVehiculoRg = self.lineEdit_ViajeVehiculoId_Registrar
        
        self.leChoferIdRg = self.lineEdit_ChoferId_Registrar
        self.leMarcaRg = self.lineEdit_Marca_Registrar
        self.SpCantPasajerosRg = self.spinBox_CapPasajeros_Registrar

        self.leChoferApellidosRg = self.lineEdit_ChoferApellidos_Registrar
        self.leChoferCedulaRg = self.lineEdit_ChoferCedula_Registrar
        self.leChoferNombresRg = self.lineEdit_ChoferNombres_Registrar

        self.leClienteApellidosRg = self.lineEdit_ClienteApellidos_Registrar
        self.leClienteCedulaRg = self.lineEdit_ClienteCedula_Registrar
        self.leClienteNombresRg = self.lineEdit_ClienteNombres_Registrar

        self.leHoraLlegadaMd = self.lineEdit_HoraLlegada_Modificar 
        self.leHoraSalidaMd = self.lineEdit_HoraSalida_Modificar
        self.leLugarDestinoMd = self.lineEdit_LugarDestino_Modificar
        self.leViajeIdClienteMd = self.lineEdit_ViajeClienteId_Modificar
        self.leViajeIdVehiculoMd = self.lineEdit_ViajeVehiculoId_Modificar
        self.leViajeIdMd = self.lineEdit_IdViaje_Modificar
        
        self.leChoferIdMd = self.lineEdit_ChoferId_Modificar
        self.leMarcaMd = self.lineEdit_Marca_Modificar
        self.leIdVehiculoMd = self.lineEdit_IdVehiculo_Modificar
        self.leCantPasajerosMd = self.lineEdit_CapPasajeros_Modificar

        self.leIdChoferMd = self.lineEdit_IdChofer_Modificar
        self.leChoferApellidosMd = self.lineEdit_ChoferApellidos_Modificar
        self.leChoferNombresMd = self.lineEdit_ChoferNombres_Modificar
        self.leChoferCedulaMd = self.lineEdit_ChoferCedula_Modificar

        self.leIdClienteMd = self.lineEdit_IdCliente_Modificar
        self.leClienteApellidosMd = self.lineEdit_ClienteApellidos_Modificar
        self.leClienteNombresMd = self.lineEdit_ClienteNombres_Modificar
        self.leClienteCedulaMd = self.lineEdit_ClienteCedula_Modificar

        self.leHoraLlegadaBs = self.lineEdit_HoraLlegada_Buscar 
        self.leHoraSalidaBs = self.lineEdit_HoraSalida_Buscar
        self.leLugarDestinoBs = self.lineEdit_LugarDestino_Buscar
        self.leViajeIdClienteBs = self.lineEdit_ViajeClienteId_Buscar
        self.leViajeIdVehiculoBs = self.lineEdit_ViajeVehiculoId_Buscar
        self.leViajeIdBs = self.lineEdit_IdViaje_Buscar
        
        self.leChoferIdBs = self.lineEdit_VehiculoChoferId_Buscar
        self.leMarcaBs = self.lineEdit_Marca_Buscar
        self.leIdVehiculoBs = self.lineEdit_IdVehiculo_Buscar
        self.leCantPasajerosBs = self.lineEdit_CapPasajeros_Buscar

        self.leIdChoferBs = self.lineEdit_IdChofer_Buscar
        self.leChoferApellidosBs = self.lineEdit_ChoferApellidos_Buscar
        self.leChoferNombresBs = self.lineEdit_ChoferNombres_Buscar
        self.leChoferCedulaBs = self.lineEdit_ChoferCedula_Buscar

        self.leIdClienteBs = self.lineEdit_IdCliente_Buscar
        self.leClienteApellidosBs = self.lineEdit_ClienteApellidos_Buscar
        self.leClienteNombresBs = self.lineEdit_ClienteNombres_Buscar
        self.leClienteCedulaBs = self.lineEdit_ClienteCedula_Buscar

        self.leIdChoferBcDel = self.lineEdit_IdChofer_Eliminar
        self.leIdClienteBcDel = self.lineEdit_IdCliente_Eliminar
        self.leIdViajeBcDel = self.lineEdit_IdViaje_Eliminar
        self.leIdVehiculoBcDel = self.lineEdit_IdVehiculo_Eliminar


        self.boxEntidadesDatos = self.Box_Entidades_Datos # Asigna el comboBox a un atributo
        self.boxEntidadesModificar = self.Box_Entidades_Modificar
        self.boxEntidadesBuscar = self.Box_Entidades_Buscar
        self.boxEntidadesRegistrar = self.Box_Entidades_Registrar
        self.boxEntidadesEliminar = self.Box_Entidades_Eliminar
        self.Db = BaseDatos()
        self.initGui()

    def initGui(self):
            # Conectar el evento clicked del boton para cambiar de pag
            self.botonDatos.clicked.connect(lambda: self.stacked_pages.setCurrentIndex(0)) 
            self.botonRegistrar.clicked.connect(lambda: self.stacked_pages.setCurrentIndex(1))   
            self.botonModificar.clicked.connect(lambda: self.stacked_pages.setCurrentIndex(2))   
            self.botonBuscar.clicked.connect(lambda: self.stacked_pages.setCurrentIndex(3)) 
            self.botonEliminar.clicked.connect(lambda: self.stacked_pages.setCurrentIndex(4))  
            # Conectar el evento clicked del boton para llamar a las funciones
            self.botonRgViaje.clicked.connect(self.registrarViaje)
            self.botonRgVehiculo.clicked.connect(self.registrarVehiculo)  
            self.botonRgChofer.clicked.connect(self.registrarChofer)  
            self.botonRgCliente.clicked.connect(self.registrarCliente) 
            self.botonMdViaje.clicked.connect(self.modificarViaje)  
            self.botonMdVehiculo.clicked.connect(self.modificarVehiculo)  
            self.botonMdChofer.clicked.connect(self.modificarChofer)  
            self.botonMdCliente.clicked.connect(self.modificarCliente)
            self.botonBcChofer.clicked.connect(self.buscarChofer)
            self.botonBcCliente.clicked.connect(self.buscarCliente)
            self.botonBcVehiculo.clicked.connect(self.buscarVehiculo)
            self.botonBcViaje.clicked.connect(self.buscarViaje)
            self.botonBcChoferDel.clicked.connect(self.buscarEliminarChofer)
            self.botonDelChofer.clicked.connect(self.eliminarChofer)
            self.botonBcClienteDel.clicked.connect(self.buscarEliminarCliente)
            self.botonDelCliente.clicked.connect(self.eliminarCliente)
            self.botonBcVehiculoDel.clicked.connect(self.buscarEliminarVehiculo)
            self.botonDelVehiculo.clicked.connect(self.eliminarVehiculo)
            self.botonBcViajeDel.clicked.connect(self.buscarEliminarViaje)
            self.botonDelViaje.clicked.connect(self.eliminarViaje)
            self.botonActualizar.clicked.connect(self.pagDatos)
            self.pagDatos()

            # Conectar el evento currentIndexChanged del QComboBox
            self.boxEntidadesDatos.currentIndexChanged.connect(self.pagEntDatos)
            self.boxEntidadesRegistrar.currentIndexChanged.connect(self.pagEntRegistrar)
            self.boxEntidadesModificar.currentIndexChanged.connect(self.pagEntModificar)
            self.boxEntidadesBuscar.currentIndexChanged.connect(self.pagEntBuscar)
            self.boxEntidadesEliminar.currentIndexChanged.connect(self.pagEntEliminar)

    def pagDatos(self):
        # Configurar el número de filas y columnas viajes
        info = self.Db.buscarTodo(0)
        self.tablaViajeDatos.setRowCount(len(info))
        for fila, datos in enumerate(info):
            for columna, dato in enumerate(datos):
                self.tablaViajeDatos.setItem(fila, columna, QTableWidgetItem(str(dato)))
        
        # Configurar el número de filas y columnas vehiculos
        info = self.Db.buscarTodo(1)
        self.tablaVehiculoDatos.setRowCount(len(info))
        for fila, datos in enumerate(info):
            for columna, dato in enumerate(datos):
                self.tablaVehiculoDatos.setItem(fila, columna, QTableWidgetItem(str(dato)))
        
        # Configurar el número de filas y columnas choferes
        info = self.Db.buscarTodo(2)
        self.tablaChoferDatos.setRowCount(len(info))
        for fila, datos in enumerate(info):
            for columna, dato in enumerate(datos):
                self.tablaChoferDatos.setItem(fila, columna, QTableWidgetItem(str(dato)))
        
        # Configurar el número de filas y columnas de clientes
        info = self.Db.buscarTodo(3)
        self.tablaClienteDatos.setRowCount(len(info))
        for fila, datos in enumerate(info):
            for columna, dato in enumerate(datos):
                self.tablaClienteDatos.setItem(fila, columna, QTableWidgetItem(str(dato)))

    def registrarChofer(self):
        nombres = self.leChoferNombresRg.text()
        apellidos = self.leChoferApellidosRg.text()
        cedula = self.leChoferCedulaRg.text()
        v = Validacion()
        if not v.esNumero(cedula) or not v.noEstaVacio(cedula) or not v.noEstaVacio(cedula):
            self.showMessageBox('Por Favor, Ingrese Cedula Correctamente')
        elif not v.noTieneNumero(nombres) or not v.noEstaVacio(nombres) or not v.noEstaVacio(nombres):
            self.showMessageBox('Por favor., Ingrese Nombre Correctamente')
        elif not v.noTieneNumero(apellidos) or not v.noEstaVacio(apellidos) or not v.noEstaVacio(apellidos):
            self.showMessageBox('Por favor, Ingrese Apellido Correctamente')
        else:
            chofer = Chofer(0, cedula, nombres, apellidos)
            self.Db.ingresar(chofer)
            self.leChoferNombresRg.setText('')
            self.leChoferApellidosRg.setText('')
            self.leChoferCedulaRg.setText('')
            self.showMessageBox('Registro Hecho Correctamente')

    def registrarCliente(self):
        nombres = self.leClienteNombresRg.text()
        apellidos = self.leClienteApellidosRg.text()
        cedula = self.leClienteCedulaRg.text()
        v = Validacion()
        if not v.esNumero(cedula) or not v.noEstaVacio(cedula) or not v.noEstaVacio(cedula):
            self.showMessageBox('Por favor, Ingrese Cedula Correctamente')
        elif not v.noTieneNumero(nombres) or not v.noEstaVacio(nombres) or not v.noEstaVacio(nombres):
            self.showMessageBox('Por Favor, Ingrese Nombre Correctamente')
        elif not v.noTieneNumero(apellidos) or not v.noEstaVacio(apellidos) or not v.noEstaVacio(apellidos):
            self.showMessageBox('Por Favor, Ingrese Apellido Correctamente')
        else:
            cliente = Cliente(0, cedula, nombres, apellidos)
            self.Db.ingresar(cliente)
            self.leClienteNombresRg.setText('')
            self.leClienteApellidosRg.setText('')
            self.leClienteCedulaRg.setText('')
            self.showMessageBox('Registro Hecho Correctamente')


    def registrarVehiculo(self):
        capPasajeros = self.SpCantPasajerosRg.text()
        marca = self.leMarcaRg.text()
        Chofer_Id = self.leChoferIdRg.text()
        v = Validacion()
        if not v.esNumero(capPasajeros) or not v.noEstaVacio(capPasajeros) or not v.noEstaVacio(capPasajeros):
            self.showMessageBox('Por Favor, Ingrese Capacidad De Pasajeros Correctamente')
        elif not v.noTieneNumero(marca) or not v.noEstaVacio(marca) or not v.noEstaVacio(marca):
            self.showMessageBox('Por Favor, Ingrese Marca Correctamente')
        elif not v.esNumero(Chofer_Id) or not v.noEstaVacio(Chofer_Id) or not v.noEstaVacio(Chofer_Id):
            self.showMessageBox('Por Favor, Ingrese Chofer Correctamente')
        elif not v.existeChofer(Chofer_Id):
            self.showMessageBox('Por Favor, Ingrese Un Chofer Existente')
        else:
            vehiculo = Vehiculo(0, capPasajeros, marca, Chofer_Id)
            self.Db.ingresar(vehiculo)
            self.SpCantPasajerosRg.setValue(1)
            self.leMarcaRg.setText('')
            self.leChoferIdRg.setText('')
            self.showMessageBox('Registro Hecho Correctamente')

    def registrarViaje(self):
        id = self.leViajeIdMd.text()
        lugarDestino = self.leLugarDestinoRg.text()
        horaLlegada = self.leHoraLlegadaRg.text()
        horaSalida = self.leHoraSalidaRg.text()
        clienteId = self.leViajeIdClienteRg.text()
        vehiculoId = self.leViajeIdVehiculoRg.text()
        v = Validacion()
        if not v.noTieneNumero(lugarDestino) or not v.noEstaVacio(lugarDestino) or not v.noEstaVacio(lugarDestino):
            self.showMessageBox('Por Favor, Ingrese Lugar De Distino Correctamente')
        elif not v.verificarHora(horaLlegada) or not v.noEstaVacio(horaLlegada) or not v.noEstaVacio(horaLlegada):
            self.showMessageBox('Por Favor, Ingrese La Hora De LLegada Correctamente: 23:59')
        elif not v.verificarHora(horaSalida) or not v.noEstaVacio(horaSalida) or not v.noEstaVacio(horaSalida):
            self.showMessageBox('Por Favor, Ingrese La Hora De Salida Correctamente: 23:59')
        elif not v.esNumero(clienteId) or not v.noEstaVacio(clienteId) or not v.noEstaVacio(clienteId):
            self.showMessageBox('Por Favor, Ingrese Cliente Correctamente')
        elif not v.existeCliente(clienteId):
            self.showMessageBox('Por Favor, Ingrese Un Cliente Existente')
        elif not v.esNumero(vehiculoId) or not v.noEstaVacio(vehiculoId) or not v.noEstaVacio(vehiculoId):
            self.showMessageBox('Por Favor, Ingrese Vehiculo Correctamente')
        elif not v.existeVehiculo(vehiculoId):
            self.showMessageBox('Por favor, Ingrese Un Vehiculo Existente')
        else:
            viaje = Viaje(id, lugarDestino, horaLlegada, horaSalida, clienteId, vehiculoId)
            self.Db.ingresar(viaje)
            id = self.leViajeIdMd.setText('')
            lugarDestino = self.leLugarDestinoRg.setText('')
            horaLlegada = self.leHoraLlegadaRg.setText('')
            horaSalida = self.leHoraSalidaRg.setText('')
            clienteId = self.leViajeIdClienteRg.setText('')
            vehiculoId = self.leViajeIdVehiculoRg.setText('')
            self.showMessageBox('Registro Hecho Correctamente')

    def modificarChofer(self):
        id = self.leIdChoferMd.text()
        nombres = self.leChoferNombresMd.text()
        apellidos = self.leChoferApellidosMd.text()
        cedula = self.leChoferCedulaMd.text()
        v = Validacion()
        if not v.esNumero(id) or not v.noEstaVacio(id) or not v.noEstaVacio(id):
            self.showMessageBox('Por Favor, Ingrese Id Correctamente')
        elif not v.existeChofer(id):
            self.showMessageBox('Por Favor, Ingrese Un Chofer Existente')
        elif not v.esNumero(cedula) or not v.noEstaVacio(cedula) or not v.noEstaVacio(cedula):
            self.showMessageBox('Por Favor, Ingrese Cedula Correctamente')
        elif not v.noTieneNumero(nombres) or not v.noEstaVacio(nombres) or not v.noEstaVacio(nombres):
            self.showMessageBox('Por favor., Ingrese Nombre Correctamente')
        elif not v.noTieneNumero(apellidos) or not v.noEstaVacio(apellidos) or not v.noEstaVacio(apellidos):
            self.showMessageBox('Por favor, Ingrese Apellido Correctamente')
        else:
            chofer = Chofer(id, cedula, nombres, apellidos)
            self.Db.modificar(chofer)
            id = self.leIdChoferMd.setText('')
            nombres = self.leChoferNombresMd.setText('')
            apellidos = self.leChoferApellidosMd.setText('')
            cedula = self.leChoferCedulaMd.setText('')
            self.showMessageBox('Registro Modificado Correctamente')

    def modificarCliente(self):
        id = self.leIdClienteMd.text()
        nombres = self.leClienteNombresMd.text()
        apellidos = self.leClienteApellidosMd.text()
        cedula = self.leClienteCedulaMd.text()
        v = Validacion()
        if not v.esNumero(id) or not v.noEstaVacio(id) or not v.noEstaVacio(id):
            self.showMessageBox('Por favor, Ingrese Id Correctamente')
        elif not v.existeCliente(id):
            self.showMessageBox('Por favor, Ingrese Un Cliente Existente')
        elif not v.esNumero(cedula) or not v.noEstaVacio(cedula) or not v.noEstaVacio(cedula):
            self.showMessageBox('Por favor, Ingrese Cedula Correctamente')
        elif not v.noTieneNumero(nombres) or not v.noEstaVacio(nombres) or not v.noEstaVacio(nombres):
            self.showMessageBox('Por Favor, Ingrese Nombre Correctamente')
        elif not v.noTieneNumero(apellidos) or not v.noEstaVacio(apellidos) or not v.noEstaVacio(apellidos):
            self.showMessageBox('Por Favor, Ingrese Apellido Correctamente')
        else:
            cliente = Cliente(id, cedula, nombres, apellidos)
            self.Db.modificar(cliente)
            self.leIdClienteMd.setText('')
            self.leClienteNombresMd.setText('')
            self.leClienteApellidosMd.setText('')
            self.leClienteCedulaMd.setText('')
            self.showMessageBox('Registro Modificado Correctamente')

    def modificarVehiculo(self):
        id = self.leIdVehiculoMd.text()
        capPasajeros = self.leCantPasajerosMd.text()
        marca = self.leMarcaMd.text()
        Chofer_Id = self.leChoferIdMd.text()
        v = Validacion()
        if not v.esNumero(id) or not v.noEstaVacio(id) or not v.noEstaVacio(id):
            self.showMessageBox('Por Favor, Ingrese Id Correctamente')
        elif not v.existeVehiculo(id):
            self.showMessageBox('Por Favor, Ingrese Un Vehiculo Existente')
        elif not v.esNumero(capPasajeros) or not v.noEstaVacio(capPasajeros) or not v.noEstaVacio(capPasajeros):
            self.showMessageBox('Por Favor, Ingrese Capacidad De Pasajeros Correctamente')
        elif not v.noTieneNumero(marca) or not v.noEstaVacio(marca) or not v.noEstaVacio(marca):
            self.showMessageBox('Por Favor, Ingrese Marca Correctamente')
        elif not v.esNumero(Chofer_Id) or not v.noEstaVacio(Chofer_Id) or not v.noEstaVacio(Chofer_Id):
            self.showMessageBox('Por Favor, Ingrese Chofer Correctamente')
        elif not v.existeChofer(Chofer_Id):
            self.showMessageBox('Por Favor, Ingrese Un Chofer Existente')
        else:
            vehiculo = Vehiculo(id, capPasajeros, marca, Chofer_Id)
            self.Db.modificar(vehiculo)
            self.leIdVehiculoMd.setText('')
            self.leCantPasajerosMd.setText('')
            self.leMarcaMd.setText('')
            self.leChoferIdMd.setText('')
            self.showMessageBox('Registro Modificado Correctamente')

    def modificarViaje(self):
        id = self.leViajeIdMd.text()
        lugarDestino = self.leLugarDestinoMd.text()
        horaLlegada = self.leHoraLlegadaMd.text()
        horaSalida = self.leHoraSalidaMd.text()
        clienteId = self.leViajeIdClienteMd.text()
        vehiculoId = self.leViajeIdVehiculoMd.text()
        v = Validacion()
        if not v.esNumero(id) or not v.noEstaVacio(id) or not v.noEstaVacio(id):
            self.showMessageBox('Por Favor, Ingrese Id Correctamente')
        elif not v.existeViaje(id):
            self.showMessageBox('Por Favor, Ingrese Un Viaje Existente')
        elif not v.noTieneNumero(lugarDestino) or not v.noEstaVacio(lugarDestino) or not v.noEstaVacio(lugarDestino):
            self.showMessageBox('Por Favor, Ingrese Lugar De Distino Correctamente')
        elif not v.verificarHora(horaLlegada) or not v.noEstaVacio(horaLlegada) or not v.noEstaVacio(horaLlegada):
            self.showMessageBox('Por Favor, Ingrese La Hora De LLegada Correctamente: 23:59')
        elif not v.verificarHora(horaSalida) or not v.noEstaVacio(horaSalida) or not v.noEstaVacio(horaSalida):
            self.showMessageBox('Por Favor, Ingrese La Hora De Salida Correctamente: 23:59')
        elif not v.esNumero(clienteId) or not v.noEstaVacio(clienteId) or not v.noEstaVacio(clienteId):
            self.showMessageBox('Por Favor, Ingrese Cliente Correctamente')
        elif not v.existeCliente(clienteId):
            self.showMessageBox('Por Favor, Ingrese Un Cliente Existente')
        elif not v.esNumero(vehiculoId) or not v.noEstaVacio(vehiculoId) or not v.noEstaVacio(vehiculoId):
            self.showMessageBox('Por Favor, Ingrese Vehiculo Correctamente')
        elif not v.existeVehiculo(vehiculoId):
            self.showMessageBox('Por favor, Ingrese Un Vehiculo Existente')
        else:
            viaje = Viaje(id, lugarDestino, horaLlegada, horaSalida, clienteId, vehiculoId)
            self.Db.modificar(viaje)
            self.leViajeIdMd.setText('')
            self.leLugarDestinoMd.setText('')
            self.leHoraLlegadaMd.setText('')
            self.leHoraSalidaMd.setText('')
            self.leViajeIdClienteMd.setText('')
            self.leViajeIdVehiculoMd.setText('')
            self.showMessageBox('Registro Modificado Correctamente')


    def buscarChofer(self):
        id = self.leIdChoferBs.text()
        v = Validacion()
        if v.esNumero(id):
            datos = self.Db.buscarId(2, id)
            if datos:
                self.leChoferCedulaBs.setText(datos[1])
                self.leChoferNombresBs.setText(datos[2])
                self.leChoferApellidosBs.setText(datos[3])
            else:
                self.showMessageBox('No Existe Ese Chofer')
                self.leChoferCedulaBs.setText('')
                self.leChoferNombresBs.setText('')
                self.leChoferApellidosBs.setText('')
        else:
            self.showMessageBox('Introduzca Un Número Valido')
            self.leChoferCedulaBs.setText('')
            self.leChoferNombresBs.setText('')
            self.leChoferApellidosBs.setText('')


    def buscarCliente(self):
        id = self.leIdClienteBs.text()
        v = Validacion()
        if v.esNumero(id):
            datos = self.Db.buscarId(3, id)
            if datos:
                self.leClienteCedulaBs.setText(datos[1])
                self.leClienteNombresBs.setText(datos[2])
                self.leClienteApellidosBs.setText(datos[3])
            else:
                self.showMessageBox('No Existe Ese Cliente')
                self.leClienteCedulaBs.setText('')
                self.leClienteNombresBs.setText('')
                self.leClienteApellidosBs.setText('')
        else:
            self.showMessageBox('Introduzca Un Número Valido')
            self.leClienteCedulaBs.setText('')
            self.leClienteNombresBs.setText('')
            self.leClienteApellidosBs.setText('')

    def buscarVehiculo(self):
        id = self.leIdVehiculoBs.text()
        v = Validacion()
        if v.esNumero(id):
            datos = self.Db.buscarId(1, id)
            if datos:
                self.leCantPasajerosBs.setText(str(datos[1]))
                self.leMarcaBs.setText(datos[2])
                self.leChoferIdBs.setText(str(datos[3]))
            else:
                self.showMessageBox('No Existe Ese Vehiculo')
                self.leCantPasajerosBs.setText('')
                self.leMarcaBs.setText('')
                self.leChoferIdBs.setText('')   
        else:
            self.showMessageBox('Introduzca Un Número Valido')
            self.leCantPasajerosBs.setText('')
            self.leMarcaBs.setText('')
            self.leChoferIdBs.setText('')


    def buscarViaje(self):
        id = self.leViajeIdBs.text()
        v = Validacion()
        if v.esNumero(id):
            datos = self.Db.buscarId(0, id)
            if datos:
                self.leLugarDestinoBs.setText(datos[1])
                self.leHoraLlegadaBs.setText(datos[2])
                self.leHoraSalidaBs.setText(datos[3])
                self.leViajeIdClienteBs.setText(str(datos[4]))
                self.leViajeIdVehiculoBs.setText(str(datos[5]))
            else:
                self.showMessageBox('No Existe Ese Viaje')
                self.leLugarDestinoBs.setText('')
                self.leHoraLlegadaBs.setText('')
                self.leHoraSalidaBs.setText('')
                self.leViajeIdClienteBs.setText('')
                self.leViajeIdVehiculoBs.setText('')
        else:
            self.showMessageBox('Introduzca Un Número Valido')
            self.leLugarDestinoBs.setText('')
            self.leHoraLlegadaBs.setText('')
            self.leHoraSalidaBs.setText('')
            self.leViajeIdClienteBs.setText('')
            self.leViajeIdVehiculoBs.setText('')

    def buscarEliminarChofer(self):
        id = self.leIdChoferBcDel.text()
        v = Validacion()
        if v.esNumero(id): 
            info = self.Db.buscarId(2, id)
            self.tablaChoferDel.setRowCount(self.verificar_info(info))
            #Agragar datos a la tabla 
            for columna, dato in enumerate(info):
                self.tablaChoferDel.setItem(0, columna, QTableWidgetItem(str(dato)))
            if not info:
                self.showMessageBox(f'Chofer Con Id {id} No Existe')
        else:
            self.showMessageBox('Introduzca Un Número Valido')
            info = []
            self.tablaChoferDel.setRowCount(0)
            for columna, dato in enumerate(info):
                self.tablaChoferDel.setItem(0, columna, QTableWidgetItem(str(dato)))

    def eliminarChofer(self):  
        id = self.leIdChoferBcDel.text()
        v = Validacion()
        if v.existeChofer(id):
            self.buscarEliminarChofer()
            if v.verificarDependenciaChoferVehiculo(2,id):
                self.showMessageBox(f'No Se Puede Eliminar El Chofer Con Id {id}')
            else:
                if self.showMessageBoxEliminar(f'Eliminar Chofer Con Id {id}?'):
                    self.Db.eliminar(id, 0)
        self.buscarEliminarChofer()
        print('Eliminado con exito')

    def buscarEliminarCliente(self):
        id = self.leIdClienteBcDel.text()
        v = Validacion()
        if v.esNumero(id):
            info = self.Db.buscarId(3, id)
            self.tablaClienteDel.setRowCount(v.verificar_info(info)) 
            #Agragar datos a la tabla 
            for columna, dato in enumerate(info):
                self.tablaClienteDel.setItem(0, columna, QTableWidgetItem(str(dato)))
            if not info:
                self.showMessageBox(f'No Existe El Cliente Con Id {id}')
        else:
            self.showMessageBox('Por Favor, Introduzca Un Número Valido')
            info = []
            self.tablaChoferDel.setRowCount(0)
            for columna, dato in enumerate(info):
                self.tablaClienteDel.setItem(0, columna, QTableWidgetItem(str(dato)))

    def eliminarCliente(self):  
        id = self.leIdClienteBcDel.text()
        v = Validacion()
        if v.esNumero(id):
            self.buscarEliminarCliente()
            if not v.verificarDependenciaClienteViaje(0, id):
                if self.showMessageBoxEliminar(f'Eliminar Cliente Con Id {id}?'):
                    self.Db.eliminar(id, 2)
            else:
                self.showMessageBox(f'No Se Puede Eliminar El Cliente Con Id {id}')
        self.buscarEliminarCliente()
        print('Eliminado con exito')

    def buscarEliminarVehiculo(self):
        id = self.leIdVehiculoBcDel.text()
        v = Validacion()
        if v.esNumero(id):
            info = self.Db.buscarId(1, id)
            self.tablaVehiculoDel.setRowCount(self.verificar_info(info))
            #Agragar datos a la tabla 
            for columna, dato in enumerate(info):
                self.tablaVehiculoDel.setItem(0, columna, QTableWidgetItem(str(dato)))
            if not info:
                self.showMessageBox(f'Vehiculo Con Id {id} No Existe')
        else:
            self.showMessageBox('Por Favor, Introduzca Un Número Valido')
            info = []
            self.tablaVehiculoDel.setRowCount(0)
            #Agragar datos a la tabla 
            for columna, dato in enumerate(info):
                self.tablaVehiculoDel.setItem(0, columna, QTableWidgetItem(str(dato)))

    def eliminarVehiculo(self):  
        id = self.leIdVehiculoBcDel.text()
        v = Validacion()
        if v.esNumero(id):
            self.buscarEliminarVehiculo()
            if not v.verificarDependenciaVehiculoViaje(1,id):
                if self.showMessageBoxEliminar(f'Eliminar Vehiculo Con Id {id}?'):
                    self.Db.eliminar(id, 1)        
            else:
                self.showMessageBox(f'No Se Puede Eliminar El vehiculo Con Id {id}')
        self.buscarEliminarVehiculo()
        print('Eliminado con exito')    

    def buscarEliminarViaje(self):
        id = self.leIdViajeBcDel.text()
        v = Validacion()
        if v.esNumero(id):
            info = self.Db.buscarId(0, id)
            self.tablaViajeDel.setRowCount(self.verificar_info(info))
            #Agragar datos a la tabla 
            for columna, dato in enumerate(info):
                self.tablaViajeDel.setItem(0, columna, QTableWidgetItem(str(dato)))
            if not info:
                self.showMessageBox(f'Viaje Con Id {id} No Existe')
        else:
            self.showMessageBox('Por Favor, Introduzca Un Número Valido')
            info = []
            self.tablaViajeDel.setRowCount(0)
            #Agragar datos a la tabla 
            for columna, dato in enumerate(info):
                self.tablaViajeDel.setItem(0, columna, QTableWidgetItem(str(dato)))
     
    def eliminarViaje(self):  
        id = self.leIdViajeBcDel.text()
        v = Validacion()
        if v.esNumero(id):
            self.buscarEliminarViaje()
            if self.showMessageBoxEliminar(f'Eliminar Vehiculo Con Id {id}?'):
                    self.Db.eliminar(id, 3)

        self.buscarEliminarViaje()


    def pagEntDatos(self, index):
        self.stacked_pages_Datos.setCurrentIndex(index)
    def pagEntRegistrar(self, index):
        self.stacked_pages_Registrar.setCurrentIndex(index)     
    def pagEntModificar(self, index):
        self.stacked_pages_Modificar.setCurrentIndex(index)
    def pagEntBuscar(self, index):
        self.stacked_pages_Buscar.setCurrentIndex(index)
    def pagEntEliminar(self, index):
        self.stacked_pages_Eliminar.setCurrentIndex(index)
    def verificar_info(self, a):
        return 0 if not a else 1

    def showMessageBox(self, texto):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText(texto)
        msgBox.setWindowTitle("Mensaje Informativo")
        msgBox.setStandardButtons(QMessageBox.Ok )
        # Mostrar el cuadro de mensaje
        retorno = msgBox.exec_()

        if retorno == QMessageBox.Ok:
            print("Has presionado OK")

    def showMessageBoxEliminar(self, texto):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText(texto)
        msgBox.setWindowTitle("Mensaje Informativo")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        # Mostrar el cuadro de mensaje
        retorno = msgBox.exec_()
        if retorno == QMessageBox.Ok:
            return True
        return False