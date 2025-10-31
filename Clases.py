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