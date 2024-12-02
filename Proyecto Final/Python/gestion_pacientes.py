from conexion import BaseDeDatos

class Pacientes:
    def __init__(self, db):
        self.db = db

    def registrar_paciente(self, nombre, fecha_nacimiento, historia_clinica):
        query = "INSERT INTO Pacientes (nombre, fecha_nacimiento, historia_clinica) VALUES (%s, %s, %s)"    
        valores = (nombre, fecha_nacimiento, historia_clinica)
        self.db.ejecutar(query, valores)
        return "Paciente Registrado con exito"

    def actualizar_paciente(self, id_paciente, nombre, fecha_nacimiento, historia_clinica):
        query = "UPDATE Pacientes SET nombre=%s, fecha_nacimiento=%s, historia_clinica=%s WHERE id_paciente = %s"
        valores = (nombre, fecha_nacimiento, historia_clinica, id_paciente)
        self.db.ejecutar(query, valores)
        return "Paciente actualizado con exito"

    def ver_paciente(self, id_paciente):
        query ="SELECT * FROM Pacientes WHERE id_paciente = %s"
        return self.db.obtener_datos(query, (id_paciente,))

    def eliminar_paciente(self, id_paciente):
        query = "DELETE FROM Pacientes WHERE id_paciente = %s"
        self.db.ejecutar(query, (id_paciente,))
        return "Paciente eliminado con éxito."
    
    def eliminar_paciente(self, id_paciente):
        self.eliminar_turno(id_paciente)
        query_paciente = "DELETE FROM Pacientes WHERE id_paciente = %s"
        self.db.ejecutar(query_paciente, (id_paciente,))
        return "Turnos y paciente eliminados con éxito."
    
    def eliminar_turno(self, id_paciente):
        query_turnos = "DELETE FROM Turnos WHERE id_paciente = %s"
        self.db.ejecutar(query_turnos, (id_paciente,))
        return "Turnos del paciente eliminados con éxito."
    
    def ver_pacientes(self):
        query = "SELECT * FROM Pacientes"
        return self.db.obtener_datos(query)
    
    def buscar_paciente_por_nombre(self, nombre):
        query = "SELECT * FROM Pacientes WHERE (nombre LIKE %s)"
        valores = (f"%{nombre}%",)
        return self.db.obtener_datos(query, valores)
