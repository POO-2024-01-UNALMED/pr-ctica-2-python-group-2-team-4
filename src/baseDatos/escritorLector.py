import os
import pickle

import pathlib


class EscritorLector:
    @classmethod
    def deserializarTodo(cls):
        from gestorAplicacion.servicios.tienda import Tienda
        from gestorAplicacion.sujetos.persona import Persona
        from gestorAplicacion.servicios.proveedor import Proveedor
        Tienda.set_tiendas(cls.deserializar("tiendas"))
        Persona.set_personas(cls.deserializar("personas"))
        Tienda.set_desempleados(cls.deserializar("empleados"))
        Proveedor.set_seis_proveedores(cls.deserializar("proveedores"))

    @classmethod
    def deserializar(cls,nombre):
        path = os.path.join(os.path.dirname(__file__), 'temp\\'+nombre + '.txt')
        #path = os.path.join(pathlib.Path(__file__).parent.parent.parent.absolute(),
        #                    "src/baseDatos/temp/" + nombre + '.txt')
        #path = os.path.abspath('temp\\' + nombre + '.txt')

        with open(path,"rb") as file:
                data=pickle.load(file)
                file.close()
                return data
            
    @classmethod
    def serializarTodo(cls):
        from gestorAplicacion.servicios.tienda import Tienda
        from gestorAplicacion.sujetos.persona import Persona
        from gestorAplicacion.servicios.proveedor import Proveedor
        cls.serializar(Tienda.get_tiendas(),"tiendas")
        cls.serializar(Persona.get_personas(),"personas")
        cls.serializar(Tienda.get_desempleados(),"empleados")
        cls.serializar(Proveedor.get_seis_proveedores(),"proveedores")

    @classmethod
    def serializar(cls,lista,nombre):
        path = os.path.join(os.path.dirname(__file__), 'temp\\'+nombre + '.txt')
        #path = os.path.join(pathlib.Path(__file__).parent.parent.parent.absolute(),
        #                    "src/baseDatos/temp/" + nombre + '.txt')
        with open(path,"wb") as file:
            pickle.dump(lista,file)