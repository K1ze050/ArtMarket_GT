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

c = Trabajo("Andres", "Sublimado","01-10-2001")
print(c)

#########################
class Inventario:
    # Lista de productos permitidos
    PRODUCTOS_VALIDOS = ["playera", "taza", "papel sublimado", "vidrio", "papel impresión"]
    
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
            
        except Exception as e:
            print(f"Error al asignar cantidad: {e}")
            self._cantidad_producto = 0
    
    def __str__(self):
        if self._producto_valido:
            return f"Inventario(producto={self.producto}, cantidad={self.cantidad_producto})"
        else:
            return f"Inventario(producto=inválido, cantidad=no asignada)"
        
d = Inventario("taza",-20)  
print(d)