from collections import defaultdict

from gestorAplicacion.sujetos.persona import Persona
from gestorAplicacion.servicios.carrito import Carrito
from gestorAplicacion.servicios.enums import Genero, Edades
from gestorAplicacion.servicios.enums import Membresia

from gestorAplicacion.servicios.enums import Membresia

class Cliente(Persona):
    def __init__(self, nombre, id, edad, genero, dinero=0, carrito=None, tienda=None):
        super().__init__(nombre, id, edad, genero)
        self._membresia = None
        self._tienda = tienda
        self._dinero = dinero
        self._carrito = carrito
        self._caja = None
        self._facturas = []


    def get_membresia(self):
        return self._membresia

    def set_membresia(self, membresia):
        self._membresia = membresia

    def get_tienda(self):
        return self._tienda

    def set_tienda(self, tienda):
        self._tienda = tienda

    def get_dinero(self):
        return self._dinero

    def set_dinero(self, dinero):
        self._dinero = dinero

    def get_carrito(self):
        return self._carrito

    def set_carrito(self, carrito):
        self._carrito = carrito

    def get_caja(self):
        return self._caja

    def set_caja(self, caja):
        self._caja = caja

    def get_facturas(self):
        return self._facturas

    def set_facturas(self, facturas):
        self._facturas = facturas

    @staticmethod
    def existe_cliente(nombre):
        for i, persona in enumerate(Persona.personas):
            if persona.nombre == nombre:
                return i
        return -1

    def mayor_edad(self):
        return self.edad >= 18

    def asignaciones(self,cliente, tienda, presupuesto_predeterminadoA,presupuesto_predeterminadoN, presupuesto_personalizado=None):
        if cliente.mayor_edad():
            carrito = Carrito(cliente, tienda, Edades.ADULTOS)
            cliente.set_tienda(tienda)
            cliente.set_carrito(carrito)
            carrito.set_cliente(cliente)
            cliente.set_dinero(
                presupuesto_personalizado if presupuesto_personalizado is not None else presupuesto_predeterminadoA)
        else:
            carrito = Carrito(cliente, tienda, Edades.MENORES)
            cliente.set_tienda(tienda)
            cliente.set_carrito(carrito)
            carrito.set_cliente(cliente)
            cliente.set_dinero(
                presupuesto_personalizado if presupuesto_personalizado is not None else presupuesto_predeterminadoN)

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
            return f"Lo siento, no tienes suficiente saldo para evolucionar a {nueva_membresia.get_nombre()}"

    @staticmethod
    def calcular_costo_evolucion(membresia_actual, nueva_membresia):
        if membresia_actual is None or nueva_membresia is None:
            return nueva_membresia.get_precio()
        return nueva_membresia.get_precio() - membresia_actual.get_precio()

    def get_facturas1(self, tienda_seleccionada):
        return [c for c in tienda_seleccionada.get_facturas() if c.get_cliente() == self]

    def get_tiendas_con_facturas(self):
        tienda_con_facturas = defaultdict(int)  # Usamos defaultdict para simplificar el conteo

        for factura in self._facturas:
            if factura:
                tienda = factura.get_tienda()
                if tienda:
                    tienda_con_facturas[tienda] += 1  # Contar las facturas por tienda

        # Devolver la lista de tiendas únicas con al menos una factura
        return list(tienda_con_facturas.keys())

    def calcular_descuento_por_membresia(self):
        if self._membresia:
            return {
                Membresia.BASICO: 0.05,
                Membresia.PREMIUM: 0.10,
                Membresia.VIP: 0.20,
            }.get(self._membresia, 0.0)
        return 0.0

    def bajar_dinero(self, cantidad):
        self._dinero -= cantidad