from typing import List
from gestorAplicacion.sujetos.persona import Persona
from gestorAplicacion.servicios.carrito import Carrito
from gestorAplicacion.servicios.enums import Genero
from gestorAplicacion.servicios.enums import Membresia

class Cliente(Persona):
    def __init__(self, nombre, id, edad, genero, dinero=0, carrito=None):
        super().__init__(nombre, id, edad, genero)
        self.membresia = None
        self.tienda = None
        self.dinero = dinero
        self.carrito = carrito
        self.caja = None
        self.facturas = []

    def set_carrito(self, carrito):
        self.carrito = carrito

    def set_caja(self, caja):
        self.caja = caja

    def set_tienda(self, tienda):
        self.tienda = tienda

    def set_dinero(self, dinero):
        self.dinero = dinero

    def set_facturas(self, facturas):
        self.facturas = facturas

    def set_membresia(self, membresia):
        self.membresia = membresia

    @staticmethod
    def existe_cliente(nombre):
        for i, persona in enumerate(Persona.personas):
            if persona.nombre == nombre:
                return i
        return -1

    def mayor_edad(self):
        return self.edad >= 18

    @staticmethod
    def asignaciones(cliente, tienda, dinero=None):
        if cliente.mayor_edad():
            carrito = Carrito(cliente, tienda, "ADULTOS")
            cliente.set_carrito(carrito)
            cliente.set_tienda(tienda)
            cliente.set_dinero(dinero if dinero else 100000)
        else:
            carrito = Carrito(cliente, tienda, "MENORES")
            cliente.set_carrito(carrito)
            cliente.set_tienda(tienda)
            cliente.set_dinero(dinero if dinero else 50000)

    @staticmethod
    def perfil_demografico(cliente):
        edad = cliente.edad
        genero = cliente.genero

        if 18 <= edad <= 26:
            return "Mujer Joven" if genero == Genero.M else "Hombre Joven"
        elif 27 <= edad <= 59:
            return "Mujer Adulta" if genero == Genero.M else "Hombre Adulto"
        elif edad >= 60:
            return "Mujer Anciana" if genero == Genero.M else "Hombre Anciano"
        else:
            return "Desconocido"

    @staticmethod
    def get_mensaje_por_perfil(perfil_demografico, membresia):
        mensajes = {
            Membresia.BASICO: "Membresía Básica:\nComo miembro Básico, %s\n- Disfruta de descuentos especiales...",
            Membresia.PREMIUM: "Membresía Premium:\nComo miembro Premium, %s\n- Obtén descuentos exclusivos...",
            Membresia.VIP: "Membresía VIP:\nComo miembro VIP, %s\n- Disfruta de los mayores descuentos...",
        }
        mensaje = mensajes.get(membresia, "Beneficios Personalizados:\nTe ofrecemos beneficios adaptados a tu perfil demográfico...")

        detalles = {
            "Mujer Joven": "disfrutarás de descuentos en productos ideales para tu estilo joven y vibrante...",
            "Mujer Adulta": "obtendrás descuentos en productos que complementan tu estilo sofisticado...",
            "Mujer Anciana": "te ofrecemos descuentos en productos adaptados a tus necesidades y confort...",
            "Hombre Joven": "tendrás descuentos en productos que se adaptan a tu estilo dinámico...",
            "Hombre Adulto": "disfrutarás de descuentos en productos que se ajustan a tu estilo profesional...",
            "Hombre Anciano": "te ofrecemos descuentos en productos que se adaptan a tus preferencias y comodidad...",
            "Desconocido": "te ofrecemos descuentos en productos seleccionados..."
        }
        
        return mensaje % detalles.get(perfil_demografico, "te ofrecemos descuentos en productos seleccionados.")

    @staticmethod
    def evolucionar_membresia(cliente, nueva_membresia):
        costo_evolucion = Cliente.calcular_costo_evolucion(cliente.membresia, nueva_membresia)
        if cliente.dinero >= costo_evolucion:
            cliente.dinero -= costo_evolucion
            cliente.set_membresia(nueva_membresia)
            return f"¡Felicidades! Ahora eres miembro de la membresía {nueva_membresia.nombre}. Tu saldo actual es {cliente.dinero}"
        else:
            return f"Lo siento, no tienes suficiente saldo para evolucionar a {nueva_membresia.nombre}"

    @staticmethod
    def calcular_costo_evolucion(membresia_actual, nueva_membresia):
        if membresia_actual is None or nueva_membresia is None:
            return nueva_membresia.get_precio()
        return nueva_membresia.get_precio() - membresia_actual.get_precio()

    def get_facturas(self, tienda_seleccionada):
        return [c for c in tienda_seleccionada.get_facturas() if c.cliente == self]

    def get_tiendas_con_facturas(self):
        tiendas = set(factura.tienda for factura in self.facturas if factura)
        return list(tiendas)

    def calcular_descuento_por_membresia(self):
        if self.membresia:
            return {
                Membresia.BASICO: 0.05,
                Membresia.PREMIUM: 0.10,
                Membresia.VIP: 0.20,
            }.get(self.membresia, 0.0)
        return 0.0

    def bajar_dinero(self, cantidad):
        self.dinero -= cantidad
