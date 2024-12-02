from conexion import BaseDeDatos


class Turno:
    def __init__(self, db):
        self.db = db

    def programar_turno(self, id_paciente, id_doctor, fecha, hora, estado):
        query = "INSERT INTO Turnos (id_paciente, id_doctor, fecha, hora, estado) VALUES (%s, %s, %s, %s, %s)"
        valores = (id_paciente, id_doctor, fecha, hora, estado)
        self.db.ejecutar(query, valores)
        return "Turno programado con éxito."

    def actualizar_turno(self, id_turno, fecha, hora, estado):
        query = "UPDATE Turnos SET fecha=%s, hora=%s, estado=%s WHERE id_turno=%s"
        valores = (fecha, hora, estado, id_turno)
        self.db.ejecutar(query, valores)
        return "Turno actualizado con éxito." 

    def ver_turno(self, id_turno):
        query = "SELECT * FROM Turnos WHERE id_turno = %s"
        return self.db.obtener_datos(query, (id_turno,))

    def cancelar_turno(self, id_turno):
        query = "UPDATE Turnos SET estado = 'Cancelado' WHERE id_turno = %s"
        self.db.ejecutar(query, (id_turno,))
        return "Turno cancelado con éxito."
    
    def reporte_turnos_top_medicos(self):
        query = """
        SELECT Doctores.nombre, COUNT(Turnos.id_turno) AS cantidad_turnos
        FROM Doctores
        JOIN Turnos ON Doctores.id_doctor = Turnos.id_doctor
        GROUP BY Doctores.id_doctor
        ORDER BY cantidad_turnos DESC
        LIMIT 3
        """
        resultados = self.db.obtener_datos(query)
        return resultados
    
    def cancelar_turnos_por_medico_y_fecha(self, id_doctor, fecha_inicio, fecha_fin):
        query = """
        UPDATE Turnos
        SET estado = 'Cancelado'
        WHERE id_doctor = %s AND fecha BETWEEN %s AND %s
        """
        valores = (id_doctor, fecha_inicio, fecha_fin)
        self.db.ejecutar(query, valores)
        return "Turno/s cancelado con exito"
    
    def eliminar_turno(self, id_turno):
        query = "DELETE FROM Turnos WHERE id_turno = %s"
        self.db.ejecutar(query, (id_turno,))
        return "Turno eliminado con éxito."