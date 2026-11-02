"""
transaccion_poo_v1.py
Semana 2 - Actividad 1, Paso 2: refactorizacion de PE a POO.

Toma las funciones de procesador_transacciones.py (Semana 1) y junta los
datos (cliente_id, tipo, monto) con su logica dentro de la clase Transaccion.

Formato de cada linea de transacciones.txt:  ClienteID,Tipo,Monto
Ejemplo:                                      C001,DEBITO,150000

Para ejecutar (desde la carpeta de este archivo):  python transaccion_poo_v1.py
"""


# 1) La CLASE: el plano que une los DATOS y la LOGICA de una sola transaccion.
#    A partir de esta UNICA definicion podemos crear tantos objetos Transaccion
#    como necesitemos (ver leer_y_almacenar_datos mas abajo): un plano,
#    muchas casas distintas.
class Transaccion:
    """Representa UNA transaccion: encapsula sus datos (atributos) y su comportamiento (metodos)."""

    # Atributo de CLASE: compartido por todos los objetos (no cambia de una
    # transaccion a otra). Aqui vive la regla "que tipos existen", en un solo
    # lugar, en vez de repetirla en cada funcion como pasaba en PE.
    TIPOS_VALIDOS = ("DEBITO", "CREDITO")

    def __init__(self, cliente_id, tipo, monto):
        """
        Constructor: Python lo ejecuta automaticamente, una sola vez, al
        instanciar un objeto -- por ejemplo con Transaccion("C001", "DEBITO", 150000).

        'self' es el objeto que se esta creando en ESE momento: cada linea
        de aqui abajo dice "guarda este dato como MIO", sin mezclarse con
        los datos de otro objeto Transaccion que exista en el programa.
        """
        self.cliente_id = cliente_id   # atributo (antes: transaccion["cliente_id"])
        self.tipo = tipo               # atributo (antes: transaccion["tipo"])
        self.monto = int(monto)        # atributo (antes: transaccion["monto"])

    def obtener_informacion(self):
        """
        METODO: una accion que el objeto ejecuta usando SUS PROPIOS atributos
        (self.cliente_id, self.tipo, self.monto), sin que se los tengan
        que pasar desde afuera como en la version de PE.
        """
        return f"{self.cliente_id} - {self.tipo} - ${self.monto:,}"

    def es_tipo_valido(self):
        """METODO: indica si el tipo de ESTA transaccion es uno de los permitidos."""
        return self.tipo in self.TIPOS_VALIDOS


# 2) Leer el archivo y crear una LISTA DE OBJETOS (ya no de diccionarios).
#    Esta es la refactorizacion clave de la Actividad 1: donde antes haciamos
#    lista_transacciones.append(diccionario), ahora hacemos
#    lista_transacciones.append(objeto).
def leer_y_almacenar_datos(nombre_archivo):
    """Lee cada linea del archivo y la convierte en un objeto Transaccion."""
    lista_transacciones = []
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            partes = linea.strip().split(",")

            # Igual que en PE: las lineas vacias o mal formadas se saltan
            # sin hacer fallar el programa.
            if len(partes) == 3:
                cliente_id, tipo, monto = partes
                # Aqui se INSTANCIA el objeto: se llama al constructor __init__
                transaccion = Transaccion(cliente_id, tipo, monto)
                # Se guarda el OBJETO en la lista, no un diccionario
                lista_transacciones.append(transaccion)
    return lista_transacciones


# 3) Funciones de gestion que ahora trabajan sobre OBJETOS, no diccionarios.
#    Nota el cambio de sintaxis: transaccion["monto"] paso a ser transaccion.monto.
def calcular_monto_total(lista_transacciones):
    """Suma el atributo .monto de todos los objetos Transaccion de la lista."""
    total_monto = 0
    for transaccion in lista_transacciones:
        total_monto = total_monto + transaccion.monto   # acceso por ATRIBUTO, no por clave
    return total_monto


def filtrar_por_tipo(lista_transacciones, tipo_filtro):
    """Devuelve solo los objetos cuyo atributo .tipo coincide con tipo_filtro."""
    return [t for t in lista_transacciones if t.tipo == tipo_filtro]


# 4) Funcion principal: el flujo se ve casi igual al de PE, pero ahora cada
#    elemento de la lista "transacciones" es un objeto que sabe describirse solo.
def ejecutar_sistema():
    """Orquesta el programa: lee, muestra, totaliza y filtra las transacciones."""
    # El archivo debe estar en la MISMA carpeta desde la que se ejecuta el
    # script; si no, Python lanza FileNotFoundError.
    transacciones = leer_y_almacenar_datos("transacciones.txt")

    print("--- Todas las transacciones ---")
    for transaccion in transacciones:
        print(transaccion.obtener_informacion())   # el objeto se describe a si mismo

    print("\nMonto total de las transacciones:", calcular_monto_total(transacciones))

    print("\n--- Solo CREDITO ---")
    for transaccion in filtrar_por_tipo(transacciones, "CREDITO"):
        print(transaccion.obtener_informacion())


# Iniciar el programa
ejecutar_sistema()
