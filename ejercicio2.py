import json


# EJERCICIO 2 - Modelo de productos y persistencia

# Punto A: Excepción personalizada
class StockInvalidoError(Exception):
    pass


# Clase base
class DispositivoEcológico:

    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    @property
    def stock(self):
        return self.__stock

    @stock.setter
    def stock(self, valor):
        if valor < 0:
            raise StockInvalidoError(
                "El stock no puede ser negativo."
            )

        self.__stock = valor

    def ficha_tecnica(self):
        return (
            f"Producto: {self.nombre} | "
            f"Precio: ${self.precio} | "
            f"Stock: {self.stock}"
        )

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "precio": self.precio,
            "stock": self.stock
        }


# Herencia y polimorfismo
class PanelSolar(DispositivoEcológico):

    def __init__(self, nombre, precio, stock, potencia, eficiencia):
        super().__init__(nombre, precio, stock)
        self.potencia = potencia
        self.eficiencia = eficiencia

    def ficha_tecnica(self):
        return (
            f"{super().ficha_tecnica()} | "
            f"Potencia: {self.potencia} W | "
            f"Eficiencia: {self.eficiencia}%"
        )

    def to_dict(self):
        datos = super().to_dict()
        datos["potencia"] = self.potencia
        datos["eficiencia"] = self.eficiencia
        return datos


# Punto B: Persistencia JSON
class GestorInventario:

    def guardar_catalogo_json(self, lista_dispositivos, ruta_archivo):
        catalogo = []

        for dispositivo in lista_dispositivos:
            catalogo.append(dispositivo.to_dict())

        with open(ruta_archivo, "w", encoding="utf-8") as archivo:
            json.dump(
                catalogo,
                archivo,
                indent=4,
                ensure_ascii=False
            )

        print("Catálogo guardado correctamente.")


# Bloque de prueba
if __name__ == "__main__":

    dispositivo = DispositivoEcológico(
        "Lámpara LED", 15000, 20
    )

    panel = PanelSolar(
        "Panel Solar Eco", 250000, 10, 450, 95
    )

    # Comprobar la excepción
    try:
        panel.stock = -5

    except StockInvalidoError as error:
        print(f"Error controlado: {error}")

    print("\n===== CATÁLOGO ECOTECH =====")

    print(dispositivo.ficha_tecnica())
    print(panel.ficha_tecnica())

    # Exportar productos válidos
    productos = [dispositivo, panel]

    gestor = GestorInventario()

    gestor.guardar_catalogo_json(
        productos,
        "catalogo_ecotech.json"
    )