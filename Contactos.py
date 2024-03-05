class Contacto:
    def __init__(self, nombre, telefono, correo_electronico):
        self.nombre = nombre
        self.telefono = telefono
        self.correo_electronico = correo_electronico

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_telefono(self):
        return self.telefono

    def set_telefono(self, telefono):
        self.telefono = telefono

    def get_correo_electronico(self):
        return self.correo_electronico

    def set_correo_electronico(self, correo_electronico):
        self.correo_electronico = correo_electronico


class Agenda:
    def __init__(self):
        self.contactos = []

    def agregar_contacto(self, contacto):
        self.contactos.append(contacto)

    def eliminar_contacto(self, nombre):
        for contacto in self.contactos:
            if contacto.get_nombre() == nombre:
                self.contactos.remove(contacto)
                break

    def buscar_contacto(self, nombre):
        for contacto in self.contactos:
            if contacto.get_nombre() == nombre:
                return contacto
        return None

    def listar_contactos(self):
        for contacto in self.contactos:
            print(f"Nombre: {contacto.get_nombre()}")
            print(f"Teléfono: {contacto.get_telefono()}")
            print(f"Correo electrónico: {contacto.get_correo_electronico()}")
            print("---")

    def buscar_imprimir(self,nombre):
        contacto = agenda.buscar_contacto(nombre)
        if contacto is not None:
            print(f"Nombre: {contacto.get_nombre()}")
            print(f"Teléfono: {contacto.get_telefono()}")
            print(f"Correo electrónico: {contacto.get_correo_electronico()}")
        else: print(f"Contacto no existe")

agenda = Agenda()

# Agregar contactos
agenda.agregar_contacto(Contacto("Ana", "123456789", "ana@ejemplo.com"))
agenda.agregar_contacto(Contacto("Juan", "987654321", "juan@ejemplo.com"))
agenda.agregar_contacto(Contacto("pedro", "23151354", "pedroz12@ejemplo.com"))

# Buscar un contacto


agenda.buscar_imprimir("An")


