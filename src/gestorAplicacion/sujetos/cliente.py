from collections import defaultdict

from gestorAplicacion.sujetos.persona import Persona
from gestorAplicacion.servicios.carrito import Carrito
from gestorAplicacion.servicios.enums import Genero, Edades
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


    def perfil_demografico(self):
        edad = self.edad
        genero = self.genero

        if 18 <= edad <= 26:
            return "MujerJoven" if genero == Genero.M else "HombreJoven"
        elif 27 <= edad <= 59:
            return "MujerAdulta" if genero == Genero.M else "HombreAdulto"
        elif edad >= 60:
            return "MujerAnciana" if genero == Genero.M else "HombreAnciano"
        else:
            return "Desconocido"

    def get_mensaje_por_perfil(self,perfil_demografico, membresia):
        # Definir los mensajes según la membresía
        from gestorAplicacion.servicios.enums import Membresia
        mensajes_por_membresia = {
            Membresia.BASICO:
               " Como miembro Básico, {}\nDisfruta de descuentos especiales según tu perfil demográfico.\nMantente al tanto de nuestras ofertas en el boletín mensual.\n"
            ,
            Membresia.PREMIUM:
                "Como miembro Premium, {}\nObtén descuentos exclusivos y acceso anticipado a las últimas tendencias.\nDisfruta de atención prioritaria en cada compra.\nParticipa en eventos exclusivos diseñados para ti.\n"
            ,
            Membresia.VIP:
                "Como miembro VIP, {}\nDisfruta de los mayores descuentos y acceso anticipado a colecciones exclusivas.\nRecibe asesoramiento personal y participa en eventos VIP diseñados especialmente para ti.\nObtén beneficios máximos adaptados a tus preferencias.\n"
           ,
            "DEFAULT": """
                Beneficios Personalizados:
                Te ofrecemos beneficios adaptados a tu perfil demográfico.
                - Disfruta de descuentos y ofertas exclusivas.
                - Consulta nuestras novedades en el boletín mensual.
            """
        }

        # Seleccionar el mensaje basado en la membresía
        mensaje = mensajes_por_membresia.get(membresia, mensajes_por_membresia["DEFAULT"])

        # Definir los mensajes por perfil demográfico
        mensajes_por_perfil = {
            "MujerJoven": "disfrutarás de descuentos en productos ideales para tu estilo joven y vibrante.¡No te pierdas nuestras ofertas!",
            "MujerAdulta": "obtendrás descuentos en productos que complementan tu estilo sofisticado.Mantente al tanto de nuestras ofertas especiales.",
            "MujerAnciana": "te ofrecemos descuentos en productos adaptados a tus necesidades y confort.Consulta nuestras ofertas en el boletín mensual.",
            "HombreJoven": "tendrás descuentos en productos que se adaptan a tu estilo dinámico.No olvides revisar el boletín mensual para novedades y ofertas.",
            "HombreAdulto": "disfrutarás de descuentos en productos que se ajustan a tu estilo profesional.Consulta nuestras ofertas en el boletín mensual.",
            "HombreAnciano": "te ofrecemos descuentos en productos que se adaptan a tus preferencias y comodidad.Revisa el boletín mensual para más detalles.",
            "DEFAULT": "te ofrecemos descuentos en productos seleccionados."
        }

        # Seleccionar el mensaje basado en el perfil demográfico
        mensaje_perfil = mensajes_por_perfil.get(perfil_demografico, mensajes_por_perfil["DEFAULT"])

        # Retornar el mensaje final
        return mensaje.format(mensaje_perfil)

    def evolucionar_membresia(self,cliente, nueva_membresia):
        costo_evolucion = Cliente.calcular_costo_evolucion(cliente.membresia, nueva_membresia)
        if cliente.dinero >= costo_evolucion:
            cliente.dinero -= costo_evolucion
            cliente.set_membresia(nueva_membresia)
            return f"Ahora eres miembro de la membresía {nueva_membresia.get_nombre()}.\n Tu saldo total quedo en: ${cliente.get_dinero()}"
        else:
            return f"Lo siento, no tienes suficiente saldo para evolucionar a {nueva_membresia.nombre}"

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