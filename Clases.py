from datetime import datetime

class Trabajo:
    def __init__(self, cliente, trabajo_pendiente, fecha_entrega):
        # Usar los setters para validación inicial
        self.cliente = cliente
        self.trabajo_pendiente = trabajo_pendiente
        self.fecha_entrega = fecha_entrega
    
    # Property y setter para cliente (dato textual)
    @property
    def cliente(self):
        return self._cliente
    
    @cliente.setter
    def cliente(self, valor):
        try:
            if not isinstance(valor, str):
                raise ValueError("El cliente debe ser un texto")
            if len(valor.strip()) == 0:
                raise ValueError("El cliente no puede estar vacío")
            self._cliente = valor
        except Exception as e:
            print(f"Error al asignar cliente: {e}")
            self._cliente = ""
    
    # Property y setter para trabajo_pendiente (dato textual)
    @property
    def trabajo_pendiente(self):
        return self._trabajo_pendiente
    
    @trabajo_pendiente.setter
    def trabajo_pendiente(self, valor):
        try:
            if not isinstance(valor, str):
                raise ValueError("El trabajo pendiente debe ser un texto")
            if len(valor.strip()) == 0:
                raise ValueError("El trabajo pendiente no puede estar vacío")
            self._trabajo_pendiente = valor
        except Exception as e:
            print(f"Error al asignar trabajo pendiente: {e}")
            self._trabajo_pendiente = ""
    
    # Property y setter para fecha_entrega (formato dd-mm-yyyy)
    @property
    def fecha_entrega(self):
        return self._fecha_entrega
    
    @fecha_entrega.setter
    def fecha_entrega(self, valor):
        try:
            # Validar que sea un string
            if not isinstance(valor, str):
                raise ValueError("La fecha debe ser un texto")
            
            # Validar el formato con guiones
            if valor.count('-') != 2:
                raise ValueError("La fecha debe tener el formato dd-mm-yyyy")
            
            # Separar día, mes y año
            partes = valor.split('-')
            if len(partes[0]) != 2 or len(partes[1]) != 2 or len(partes[2]) != 4:
                raise ValueError("El formato debe ser dd-mm-yyyy (ejemplo: 25-12-2024)")
            
            # Intentar convertir el string a fecha con formato dd-mm-yyyy
            fecha_obj = datetime.strptime(valor, "%d-%m-%Y")
            self._fecha_entrega = fecha_obj
            
        except ValueError as e:
            print(f"Error al asignar fecha de entrega: {e}")
            self._fecha_entrega = None
        except Exception as e:
            print(f"Error inesperado al asignar fecha: {e}")
            self._fecha_entrega = None
    
    def imprimir_fecha(self):
        """Imprime la fecha de entrega en formato dd-mm-yyyy"""
        if self._fecha_entrega:
            print(f"Fecha de entrega: {self._fecha_entrega.strftime('%d-%m-%Y')}")
        else:
            print("Fecha de entrega: No asignada")
    
    def __str__(self):
        fecha_str = self._fecha_entrega.strftime("%d-%m-%Y") if self._fecha_entrega else "Sin fecha"
        return f"Trabajo(cliente={self.cliente}, trabajo_pendiente={self.trabajo_pendiente}, fecha_entrega={fecha_str})"


class Inventario:
    # Lista de productos permitidos
    PRODUCTOS_VALIDOS = ["playera", "taza", "papel sublimado", "vidrio", "papel impresión"]
    
    # Almacenamiento de inventario (diccionario con producto como clave y cantidad como valor)
    almacen = {}
    
    def __init__(self, producto, cantidad_producto):
        # Inicializar bandera de producto válido
        self._producto_valido = False
        # Usar los setters para validación inicial
        self.producto = producto
        self.cantidad_producto = cantidad_producto
    
    # Property y setter para producto
    @property
    def producto(self):
        return self._producto
    
    @producto.setter
    def producto(self, valor):
        try:
            # Validar que sea un string
            if not isinstance(valor, str):
                raise ValueError("El producto debe ser un texto")
            
            # Convertir a minúsculas
            valor_minuscula = valor.lower().strip()
            
            # Validar que esté en la lista de productos válidos
            if valor_minuscula not in self.PRODUCTOS_VALIDOS:
                raise ValueError(f"El producto '{valor}' no es válido. Productos permitidos: {', '.join(self.PRODUCTOS_VALIDOS)}")
            
            # Si pasa todas las validaciones
            self._producto = valor_minuscula
            self._producto_valido = True
            
        except Exception as e:
            print(f"Error al asignar producto: {e}")
            self._producto = ""
            self._producto_valido = False
    
    # Property y setter para cantidad_producto
    @property
    def cantidad_producto(self):
        return self._cantidad_producto
    
    @cantidad_producto.setter
    def cantidad_producto(self, valor):
        try:
            # Verificar primero si el producto es válido
            if not self._producto_valido:
                raise ValueError("No se puede asignar cantidad porque el producto no es válido")
            
            # Validar que sea un número
            if not isinstance(valor, (int, float)):
                raise ValueError("La cantidad debe ser un valor numérico")
            
            # Validar que no sea negativo
            if valor < 0:
                raise ValueError("La cantidad no puede ser negativa")
            
            # Validar que no esté vacío (diferente de cero)
            if valor == 0:
                raise ValueError("La cantidad no puede ser cero")
            
            self._cantidad_producto = valor
            
            # GUARDAR EN EL ALMACÉN si todo es válido
            self._guardar_en_almacen()
            
        except Exception as e:
            print(f"Error al asignar cantidad: {e}")
            self._cantidad_producto = 0
    
    def _guardar_en_almacen(self):
        """Método privado para guardar el producto y cantidad en el almacén"""
        if self._producto_valido and self._cantidad_producto > 0:
            # Si el producto ya existe, sumar la cantidad
            if self._producto in Inventario.almacen:
                Inventario.almacen[self._producto] += self._cantidad_producto
                print(f"✓ Producto '{self._producto}' actualizado en almacén. Nueva cantidad: {Inventario.almacen[self._producto]}")
            else:
                # Si es nuevo, agregarlo al almacén
                Inventario.almacen[self._producto] = self._cantidad_producto
                print(f"✓ Producto '{self._producto}' agregado al almacén con cantidad: {self._cantidad_producto}")
    
    def __str__(self):
        if self._producto_valido:
            return f"Inventario(producto={self.producto}, cantidad={self.cantidad_producto})"
        else:
            return f"Inventario(producto=inválido, cantidad=no asignada)"


class Mostrar_almacen:
    """Clase para mostrar el inventario almacenado"""
    
    def __init__(self):
        self.mostrar()
    
    def mostrar(self):
        """Muestra todo el inventario almacenado"""
        print("\n" + "="*10)
        print(" "*5 + "INVENTARIO ALMACENADO")
        print("="*10)
        
        if not Inventario.almacen:
            print("  ⚠ El almacén está vacío")
        else:
            print(f"\n  Total de productos diferentes: {len(Inventario.almacen)}")
            print("\n  Productos en stock:")
            print("  " + "-"*12)
            
            for producto, cantidad in Inventario.almacen.items():
                print(f"    • {producto.capitalize():20} : {cantidad:>6} unidades")
            
            # Calcular total de unidades
            total_unidades = sum(Inventario.almacen.values())
            print("  " + "-"*46)
            print(f"    TOTAL DE UNIDADES: {total_unidades:>6}")
        
        print("="*10 + "\n")


class Buscar_en_almacen:
    """Clase para buscar productos en el almacén usando Hashing"""
    
    def __init__(self, producto_buscar):
        self.producto_buscar = producto_buscar
        self.buscar()
    
    def buscar(self):
        """Busca un producto en el almacén usando Hashing (acceso directo por clave)"""
        print("\n" + "="*10)
        print(" "*5 + "BÚSQUEDA EN ALMACÉN")
        print("="*10)
        
        # Normalizar la búsqueda a minúsculas
        producto_normalizado = self.producto_buscar.lower().strip()
        
        print(f"\n  Buscando: '{self.producto_buscar}'")
        print(f" Producto normalizado: '{producto_normalizado}'")
        print(f" Usando Hashing (acceso directo por clave)...")
        
        # HASHING: Acceso directo O(1) usando el producto como clave del diccionario
        # El diccionario en Python usa una tabla hash internamente
        if producto_normalizado in Inventario.almacen:
            cantidad = Inventario.almacen[producto_normalizado]
            print(f"\n ¡PRODUCTO ENCONTRADO!")
            print(f" Producto: {producto_normalizado.capitalize()}")
            print(f" Cantidad en stock: {cantidad} unidades")
        else:
            print(f"\n PRODUCTO NO ENCONTRADO")
            print(f"  El producto '{self.producto_buscar}' no está en el almacén")
            
            # Sugerencias de productos disponibles
            if Inventario.almacen:
                print(f"\nProductos disponibles en almacén:")
                for prod in Inventario.almacen.keys():
                    print(f"     - {prod.capitalize()}")
        
        print("="*10 + "\n")
    
    def obtener_cantidad(self):
        """Retorna la cantidad del producto buscado (si existe)"""
        producto_normalizado = self.producto_buscar.lower().strip()
        return Inventario.almacen.get(producto_normalizado, 0)


# Menú principal del sistema
def menu_principal():
    """Menú interactivo para usar todas las clases del sistema"""
    
    while True:
        print("\n" + "="*10)
        print(" "*15 + "SISTEMA DE GESTIÓN")
        print("="*10)
        print("\n  Seleccione una opción:\n")
        print("  1. Registrar un trabajo")
        print("  2. Agregar producto al inventario")
        print("  3. Mostrar almacén completo")
        print("  4. Buscar producto en almacén")
        print("  5. Salir del programa")
        print("\n" + "="*10)
        
        try:
            opcion = input("\n Ingrese su opción (1-5): ").strip()
            
            if opcion == "1":
                registrar_trabajo()
            elif opcion == "2":
                agregar_inventario()
            elif opcion == "3":
                Mostrar_almacen()
            elif opcion == "4":
                buscar_producto()
            elif opcion == "5":
                print("\n" + "="*10)
                print(" "*5 + "Gracias por tu uso")
                print("="*10 + "\n")
                break
            else:
                print("\n  ❌ Opción inválida. Por favor ingrese un número del 1 al 5.")
                input("\n  Presione ENTER para continuar...")
        
        except KeyboardInterrupt:
            print("\n\n" + "="*10)
            print(" "*5 + "Programa interrumpido por el usuario")
            print("="*10 + "\n")
            break
        except Exception as e:
            print(f"\n  ❌ Error inesperado: {e}")
            input("\n  Presione ENTER para continuar...")


def registrar_trabajo():
    """Función para registrar un nuevo trabajo"""
    print("\n" + "-"*10)
    print(" "*15 + "REGISTRAR TRABAJO")
    print("-"*10)
    
    try:
        cliente = input("\n  Ingrese el nombre del cliente: ")
        trabajo_pendiente = input("  Ingrese el trabajo pendiente: ")
        fecha_entrega = input("  Ingrese la fecha de entrega (dd-mm-yyyy): ")
        
        trabajo = Trabajo(cliente=cliente, trabajo_pendiente=trabajo_pendiente, fecha_entrega=fecha_entrega)
        
        print("\n  ✅ Trabajo registrado exitosamente:")
        print(f"  {trabajo}")
        trabajo.imprimir_fecha()
        
    except Exception as e:
        print(f"\n Error al registrar trabajo: {e}")
    
    input("\n  Presione ENTER para volver al menú...")


def agregar_inventario():
    """Función para agregar productos al inventario"""
    print("\n" + "-"*60)
    print(" "*15 + "AGREGAR AL INVENTARIO")
    print("-"*60)
    
    print("\n  Productos válidos:")
    for i, prod in enumerate(Inventario.PRODUCTOS_VALIDOS, 1):
        print(f"    {i}. {prod.capitalize()}")
    
    try:
        producto = input("\n  Ingrese el nombre del producto: ")
        cantidad = input("  Ingrese la cantidad: ")
        
        # Intentar convertir la cantidad a número
        try:
            cantidad = float(cantidad)
        except ValueError:
            print("\n La cantidad debe ser un número válido")
            input("\n Presione ENTER para volver al menú...")
            return
        
        inventario = Inventario(producto=producto, cantidad_producto=cantidad)
        
    except Exception as e:
        print(f"\nError al agregar inventario: {e}")
    
    input("\n  Presione ENTER para volver al menú...")


def buscar_producto():
    """Función para buscar un producto en el almacén"""
    print("\n" + "-"*10)
    print(" "*17 + "BUSCAR PRODUCTO")
    print("-"*10)
    
    try:
        producto = input("\n  Ingrese el nombre del producto a buscar: ")
        
        if producto.strip() == "":
            print("\nDebe ingresar un nombre de producto")
        else:
            Buscar_en_almacen(producto)
        
    except Exception as e:
        print(f"\nError al buscar producto: {e}")
    
    input("\n  Presione ENTER para volver al menú...")

menu_principal()