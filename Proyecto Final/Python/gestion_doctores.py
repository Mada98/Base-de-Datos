from conexion import BaseDeDatos


class Doctores:
    def __init__(self, db):
        self.db = db

    def Agregar_doctor(self, nombre, especialidad):
        query = "INSERT INTO Doctores (nombre, especialidad) VALUES (%s, %s)"
        valores = (nombre, especialidad)
        self.db.ejecutar(query, valores)
        return "Doctor registrado con exito"
    
    def Actualizar_doctor(self, id_doctor, nombre, especialidad):
        query = "UPDATE Doctores SET nombre=%s, especialidad=%s WHERE id_doctor=%s"
        valores = (nombre, especialidad, id_doctor)
        self.db.ejecutar(query, valores)
        return "Doctor actualizado con exito"
    
    def ver_doctor(self, id_doctor):
        query = "SELECT * FROM Doctores WHERE id_doctor = %s"
        return self.db.obtener_datos(query, (id_doctor,))

    def eliminar_doctor(self, id_doctor):
        resultado_turnos = self.eliminar_turno(id_doctor)  
        query_doctor = "DELETE FROM Doctores WHERE id_doctor = %s"
        self.db.ejecutar(query_doctor, (id_doctor,))
        return f"{resultado_turnos} Doctor eliminado con éxito."
    
    def eliminar_turno(self, id_doctor):
        query_turnos = "DELETE FROM Turnos WHERE id_doctor = %s"
        self.db.ejecutar(query_turnos, (id_doctor,))
        return "Turnos del doctor eliminados con éxito."

    def ver_doctores(self):
        query = "SELECT * FROM Doctores"
        return self.db.obtener_datos(query)
    
    def buscar_doctor_por_nombre(self, nombre):
        query = "SELECT * FROM Doctores WHERE (nombre LIKE %s)"
        valores = (f"%{nombre}%",)
        return self.db.obtener_datos(query, valores)
    
    def buscar_doctor_por_especialidad(self, especialidad):
        query = "SELECT * FROM Doctores WHERE (especialidad LIKE %s)"
        valores = (f"%{especialidad}%",)
        return self.db.obtener_datos(query, valores)