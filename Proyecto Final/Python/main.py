import tkinter as tk
from tkinter import messagebox, simpledialog, Toplevel
from conexion import BaseDeDatos
from gestion_doctores import Doctores
from gestion_pacientes import Pacientes
from gestion_turnos import Turno
from datetime import datetime

db = BaseDeDatos(host="localhost", user="root", password="password", database="Hospital")
db.conectar()

gestion_pacientes_db = Pacientes(db)
gestion_doctores_db = Doctores(db)
gestion_turnos_db = Turno(db)

root = tk.Tk()
root.title("Gestión de Hospital")

def mostrar_busqueda_paciente():
    ventana = Toplevel(root)
    ventana.title("Buscar Paciente")

    tk.Label(ventana, text="Buscar por Nombre").grid(row=0, column=0, columnspan=2, pady=(10, 0))
    tk.Label(ventana, text="Nombre:").grid(row=1, column=0, sticky = "e")
    nombre = tk.Entry(ventana, width=30)
    nombre.grid(row=1, column=1, padx=5, pady=2)

    tk.Label(ventana, text="Buscar por ID:").grid(row=3, column=0, columnspan=2, pady=(20, 0))
    tk.Label(ventana, text="ID:").grid(row=4, column=0, sticky="e")
    id_paciente = tk.Entry(ventana, width=30)    
    id_paciente.grid(row=4, column=1, padx=5, pady=5)   

    tk.Label(ventana, text="Buscar todos los pacientes").grid(row=7, column=0, columnspan=2, pady=(20, 0))                

    def buscarNombre():
        ventana_resultados = Toplevel(ventana)
        ventana_resultados.title("Resultados de Búsqueda por Nombre")

        listbox_resultados = tk.Listbox(ventana_resultados, width=60, height=5)
        listbox_resultados.pack(padx=10, pady=10)

        resultados = gestion_pacientes_db.buscar_paciente_por_nombre(nombre.get())
        for paciente in resultados:
            listbox_resultados.insert(tk.END, paciente)

    tk.Button(ventana, text="Buscar", command=buscarNombre).grid(row=2, column=0, columnspan=2, pady=5)

    def buscarID():
        ventana_resultados = Toplevel(ventana)
        ventana_resultados.title("Resultados de Búsqueda por ID")

        listbox_resultados = tk.Listbox(ventana_resultados, width=60, height=5)
        listbox_resultados.pack(padx=10, pady=10)

        resultados = gestion_pacientes_db.ver_paciente(id_paciente.get())
        for paciente in resultados:
            listbox_resultados.insert(tk.END, paciente)

    tk.Button(ventana, text="Buscar", command=buscarID).grid(row=6, column=0, columnspan=2, pady=5)

    def buscarPacientes():
        ventana_resultados = Toplevel(ventana)
        ventana_resultados.title("Resultado de todos los pacientes")

        listbox_resultados = tk.Listbox(ventana_resultados, width=60, height=5)
        listbox_resultados.pack(padx=10, pady=10)

        resultados = gestion_pacientes_db.ver_pacientes()
        for paciente in resultados:
            listbox_resultados.insert(tk.END, paciente)

    tk.Button(ventana, text="Buscar", command=buscarPacientes).grid(row=8, column=0, columnspan=2, pady=5)

def modificar_pacientes():
    ventana = Toplevel(root)
    ventana.title("Modificar pacientes")


    tk.Label(ventana, text="ID del Paciente a Modificar:").grid(row=0, column=0, pady=5)
    id_modificar = tk.Entry(ventana, width=30)
    id_modificar.grid(row=0, column=1, pady=5)


    tk.Label(ventana, text="Nuevo Nombre:").grid(row=1, column=0, pady=5)
    nuevo_nombre = tk.Entry(ventana, width=30)
    nuevo_nombre.grid(row=1, column=1, pady=5)

    tk.Label(ventana, text="Nueva Fecha de Nacimiento:").grid(row=2, column=0, pady=5)
    nueva_fecha = tk.Entry(ventana, width=30)
    nueva_fecha.grid(row=2, column=1, pady=5)

    tk.Label(ventana, text="Nueva Historia Clínica:").grid(row=3, column=0, pady=5)
    nueva_historia = tk.Entry(ventana, width=30)
    nueva_historia.grid(row=3, column=1, pady=5)


    def cargar_datos_paciente():
        id_paciente = id_modificar.get()
        paciente = gestion_pacientes_db.ver_paciente(id_paciente)
        if paciente: 
            nuevo_nombre.delete(0, tk.END)
            nuevo_nombre.insert(0, paciente[0][1])  
            nueva_fecha.delete(0, tk.END)
            nueva_fecha.insert(0, paciente[0][2])  
            nueva_historia.delete(0, tk.END)
            nueva_historia.insert(0, paciente[0][3])  
        else:
            messagebox.showerror("Error", "Paciente no encontrado.")


    tk.Button(ventana, text="Cargar Datos", command=cargar_datos_paciente).grid(row=4, column=0, columnspan=2, pady=10)


    def guardar_modificaciones():
        id_paciente_mod = id_modificar.get()
        nombre_mod = nuevo_nombre.get()
        fecha_mod = nueva_fecha.get()
        historia_mod = nueva_historia.get()


        resultado = gestion_pacientes_db.actualizar_paciente(id_paciente_mod, nombre_mod, fecha_mod, historia_mod)
        messagebox.showinfo("Éxito", resultado)

        ventana.destroy()

    tk.Button(ventana, text="Guardar Cambios", command=guardar_modificaciones).grid(row=5, column=0, columnspan=2, pady=10)


def agregar_paciente():
    ventana = Toplevel(root)
    ventana.title("Agregar Paciente")
    
    tk.Label(ventana, text="ID del Paciente:").grid(row=0, column=0, sticky="e", padx=10, pady=5)
    tk.Label(ventana, text="Nombre:").grid(row=1, column=0, sticky="e", padx=10, pady=5)
    tk.Label(ventana, text="Fecha de Nacimiento:").grid(row=2, column=0, sticky="e", padx=10, pady=5)
    tk.Label(ventana, text="Historia Clínica:").grid(row=3, column=0, sticky="e", padx=10, pady=5)
    
    id_paciente_entry = tk.Entry(ventana, width=30)
    id_paciente_entry.grid(row=0, column=1, padx=10, pady=5)
    
    nombre_entry = tk.Entry(ventana, width=30)
    nombre_entry.grid(row=1, column=1, padx=10, pady=5)
    
    fecha_nacimiento_entry = tk.Entry(ventana, width=30)
    fecha_nacimiento_entry.grid(row=2, column=1, padx=10, pady=5)
    
    historia_clinica_entry = tk.Entry(ventana, width=30)
    historia_clinica_entry.grid(row=3, column=1, padx=10, pady=5)
    
    def guardar_paciente():
        id_paciente = id_paciente_entry.get()
        nombre = nombre_entry.get()
        fecha_nacimiento = fecha_nacimiento_entry.get()
        historia_clinica = historia_clinica_entry.get()

        try:
            datetime.strptime(fecha_nacimiento, "%Y-%m-%d")
        except ValueError:
 
                messagebox.showwarning("Formato de fecha incorrecto", 
                                   "El formato de la fecha debe ser: YYYY-MM-DD. Por favor, ingrese una fecha valida.")
                return

        paciente_existente = gestion_pacientes_db.ver_paciente(id_paciente)
        
        if paciente_existente:
            tk.messagebox.showwarning("Advertencia", "Ya existe un paciente con ese ID.")
            return
        
        resultado = gestion_pacientes_db.registrar_paciente(nombre, fecha_nacimiento, historia_clinica)
        
        tk.messagebox.showinfo("Éxito", resultado)
        ventana.destroy()  

    tk.Button(ventana, text="Guardar", command=guardar_paciente).grid(row=4, column=0, columnspan=2, pady=10)
 
def eliminar_paciente():
    ventana_eliminar = tk.Toplevel(root)
    ventana_eliminar.title("Eliminar Paciente")

    tk.Label(ventana_eliminar, text="ID del paciente a eliminar:").grid(row=0, column=0, padx=10, pady=10)
    id_paciente_entry = tk.Entry(ventana_eliminar)
    id_paciente_entry.grid(row=0, column=1, padx=10, pady=10)

    def confirmar_eliminacion():


        id_paciente = id_paciente_entry.get()
        
        paciente_existente = gestion_pacientes_db.ver_paciente(id_paciente)
        
        if not paciente_existente:
            messagebox.showwarning("Advertencia", "No se encontró un paciente con ese ID.")
            return

        resultado = gestion_pacientes_db.eliminar_paciente(id_paciente)
        
        messagebox.showinfo("Éxito", resultado)
        ventana_eliminar.destroy()  

    tk.Button(ventana_eliminar, text="Eliminar", command=confirmar_eliminacion).grid(row=1, column=0, columnspan=2, pady=10)

def mostrar_busqueda_Doctores():
    ventana = Toplevel(root)
    ventana.title("Buscar Doctor")

    tk.Label(ventana, text="Buscar por Nombre").grid(row=0, column=0, columnspan=2, pady=(10, 0))
    tk.Label(ventana, text="Nombre:").grid(row=1, column=0, sticky = "e")
    nombre = tk.Entry(ventana, width=30)
    nombre.grid(row=1, column=1, padx=5, pady=2)

    tk.Label(ventana, text="Buscar por ID:").grid(row=3, column=0, columnspan=2, pady=(20, 0))
    tk.Label(ventana, text="ID:").grid(row=4, column=0, sticky="e")
    id_doctor = tk.Entry(ventana, width=30)    
    id_doctor.grid(row=4, column=1, padx=5, pady=5)   

    tk.Label(ventana, text="Buscar por Especialidad").grid(row=7, column=0, columnspan=2, pady=(10, 0))
    tk.Label(ventana, text="Especialidad:").grid(row=8, column=0, sticky = "e")
    especialidad = tk.Entry(ventana, width=30)
    especialidad.grid(row=8, column=1, padx=5, pady=2)

    tk.Label(ventana, text="Buscar todos los doctores").grid(row=13, column=0, columnspan=2, pady=(20, 0))                

    def buscarNombre():
        ventana_resultados = Toplevel(ventana)
        ventana_resultados.title("Resultados de Búsqueda por Nombre")

        listbox_resultados = tk.Listbox(ventana_resultados, width=60, height=5)
        listbox_resultados.pack(padx=10, pady=10)

        resultados = gestion_doctores_db.buscar_doctor_por_nombre(nombre.get())
        for doctor in resultados:
            listbox_resultados.insert(tk.END, doctor)

    tk.Button(ventana, text="Buscar", command=buscarNombre).grid(row=2, column=0, columnspan=2, pady=5)

    def buscarID():
        ventana_resultados = Toplevel(ventana)
        ventana_resultados.title("Resultados de Búsqueda por ID")

        listbox_resultados = tk.Listbox(ventana_resultados, width=60, height=5)
        listbox_resultados.pack(padx=10, pady=10)

        resultados = gestion_doctores_db.ver_doctor(id_doctor.get())
        for doctor in resultados:
            listbox_resultados.insert(tk.END, doctor)

    tk.Button(ventana, text="Buscar", command=buscarID).grid(row=6, column=0, columnspan=2, pady=5)

    def buscarEspecialidad():
        ventana_resultados = Toplevel(ventana)
        ventana_resultados.title("Resultados de Búsqueda por Especialidad")

        listbox_resultados = tk.Listbox(ventana_resultados, width=60, height=5)
        listbox_resultados.pack(padx=10, pady=10)

        resultados = gestion_doctores_db.buscar_doctor_por_especialidad(especialidad.get())
        for doctor in resultados:
            listbox_resultados.insert(tk.END, doctor)

    tk.Button(ventana, text="Buscar", command=buscarEspecialidad).grid(row=11, column=0, columnspan=2, pady=5)


    def buscarDoctores():
        ventana_resultados = Toplevel(ventana)
        ventana_resultados.title("Resultado de todos los doctores")

        listbox_resultados = tk.Listbox(ventana_resultados, width=60, height=5)
        listbox_resultados.pack(padx=10, pady=10)

        resultados = gestion_doctores_db.ver_doctores()
        for paciente in resultados:
            listbox_resultados.insert(tk.END, paciente)

    tk.Button(ventana, text="Buscar", command=buscarDoctores).grid(row=14, column=0, columnspan=2, pady=5)

def agregar_Doctor():
    ventana = Toplevel(root)
    ventana.title("Agregar Doctor")
    
    tk.Label(ventana, text="ID del doctor:").grid(row=0, column=0, sticky="e", padx=10, pady=5)
    tk.Label(ventana, text="Nombre:").grid(row=1, column=0, sticky="e", padx=10, pady=5)
    tk.Label(ventana, text="Especialidad:").grid(row=3, column=0, sticky="e", padx=10, pady=5)
    
    id_doctor_entrada = tk.Entry(ventana, width=30)
    id_doctor_entrada.grid(row=0, column=1, padx=10, pady=5)
    
    nombre_entrada = tk.Entry(ventana, width=30)
    nombre_entrada.grid(row=1, column=1, padx=10, pady=5)
    
    especialidad_entrada = tk.Entry(ventana, width=30)
    especialidad_entrada.grid(row=3, column=1, padx=10, pady=5)
    
    def guardar_doctor():
        id_doctor = id_doctor_entrada.get()
        nombre = nombre_entrada.get()
        especialidad = especialidad_entrada.get()

        doctor_existente = gestion_doctores_db.ver_doctor(id_doctor)
        
        if doctor_existente:
            tk.messagebox.showwarning("Advertencia", "Ya existe un doctor con ese ID.")
            return
        
        resultado = gestion_doctores_db.Agregar_doctor(nombre, especialidad)
        
        tk.messagebox.showinfo("Éxito", resultado)
        ventana.destroy()  

    tk.Button(ventana, text="Guardar", command=guardar_doctor).grid(row=4, column=0, columnspan=2, pady=10)

def modificar_Doctores():
    ventana = Toplevel(root)
    ventana.title("Modificar doctores")

    tk.Label(ventana, text="ID del Doctor a Modificar:").grid(row=0, column=0, pady=5)
    id_modificar = tk.Entry(ventana, width=30)
    id_modificar.grid(row=0, column=1, pady=5)

    tk.Label(ventana, text="Nuevo Nombre:").grid(row=1, column=0, pady=5)
    nuevo_nombre = tk.Entry(ventana, width=30)
    nuevo_nombre.grid(row=1, column=1, pady=5)

    tk.Label(ventana, text="Nueva Especialidad:").grid(row=3, column=0, pady=5)
    nueva_especialidad = tk.Entry(ventana, width=30)
    nueva_especialidad.grid(row=3, column=1, pady=5)


    def cargar_datos_doctores():
        id_doctor = id_modificar.get()
        doctor = gestion_doctores_db.ver_doctor(id_doctor)
        if doctor: 
            nuevo_nombre.delete(0, tk.END)
            nuevo_nombre.insert(0, doctor[0][1])  
            nueva_especialidad.delete(0, tk.END)
            nueva_especialidad.insert(0, doctor[0][2])  
        else:
            messagebox.showerror("Error", "Doctor no encontrado.")


    tk.Button(ventana, text="Cargar Datos", command=cargar_datos_doctores).grid(row=4, column=0, columnspan=2, pady=10)


    def guardar_modificaciones():
        id_doctor_mod = id_modificar.get()
        nombre_mod = nuevo_nombre.get()
        especialidad_mod = nueva_especialidad.get()


        resultado = gestion_doctores_db.Actualizar_doctor(id_doctor_mod, nombre_mod, especialidad_mod)
        messagebox.showinfo("Éxito", resultado)

        ventana.destroy()

    tk.Button(ventana, text="Guardar Cambios", command=guardar_modificaciones).grid(row=5, column=0, columnspan=2, pady=10)


def eliminar_doctor():
    ventana_eliminar = tk.Toplevel(root)
    ventana_eliminar.title("Eliminar Doctor")

    tk.Label(ventana_eliminar, text="ID del doctor a eliminar:").grid(row=0, column=0, padx=10, pady=10)
    id_doctor_entry = tk.Entry(ventana_eliminar)
    id_doctor_entry.grid(row=0, column=1, padx=10, pady=10)

    def confirmar_eliminacion():

        id_doctor = id_doctor_entry.get()
        
        doctor_existente = gestion_doctores_db.ver_doctor(id_doctor)
        
        if not doctor_existente:
            messagebox.showwarning("Advertencia", "No se encontró un doctor con ese ID.")
            return

        resultado = gestion_doctores_db.eliminar_doctor(id_doctor)
        
        messagebox.showinfo("Éxito", resultado)
        ventana_eliminar.destroy()  

    tk.Button(ventana_eliminar, text="Eliminar", command=confirmar_eliminacion).grid(row=1, column=0, columnspan=2, pady=10)

def programar_turno():
    ventana = Toplevel(root)
    ventana.title("Programar Turno")

    tk.Label(ventana, text="ID Paciente:").grid(row=0, column=0)
    tk.Label(ventana, text="ID Doctor:").grid(row=1, column=0)
    tk.Label(ventana, text="Fecha (YYYY-MM-DD):").grid(row=2, column=0)
    tk.Label(ventana, text="Hora (HH:MM:SS):").grid(row=3, column=0)
    tk.Label(ventana, text="Estado:").grid(row=4, column=0)

    id_paciente = tk.Entry(ventana)
    id_doctor = tk.Entry(ventana)
    fecha = tk.Entry(ventana)
    hora = tk.Entry(ventana)
    estado = tk.Entry(ventana)

    id_paciente.grid(row=0, column=1)
    id_doctor.grid(row=1, column=1)
    fecha.grid(row=2, column=1)
    hora.grid(row=3, column=1)
    estado.grid(row=4, column=1)

    def guardar_turno():
        try:
            mensaje = gestion_turnos_db.programar_turno(
                id_paciente.get(),
                id_doctor.get(),
                fecha.get(),
                hora.get(),
                estado.get()
            )
            messagebox.showinfo("Éxito", mensaje)
            ventana.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    tk.Button(ventana, text="Guardar", command=guardar_turno).grid(row=5, column=0, columnspan=2)


def ver_turno():
    ventana = Toplevel(root)
    ventana.title("Ver Turno")

    tk.Label(ventana, text="ID Turno:").grid(row=0, column=0)

    id_turno = tk.Entry(ventana)
    id_turno.grid(row=0, column=1)

    listbox_resultados = tk.Listbox(ventana, width=60)
    listbox_resultados.grid(row=2, column=0, columnspan=2)

    def buscar_turno():
        try:
            resultados = gestion_turnos_db.ver_turno(id_turno.get())
            listbox_resultados.delete(0, tk.END)
            if resultados:
                for turno in resultados:
                    listbox_resultados.insert(tk.END, turno)
            else:
                listbox_resultados.insert(tk.END, "No se encontró el turno.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    tk.Button(ventana, text="Buscar", command=buscar_turno).grid(row=1, column=0, columnspan=2)


def cancelar_turno():
    ventana = Toplevel(root)
    ventana.title("Cancelar Turno")

    
    tk.Label(ventana, text="Cancelar Turno por ID:").grid(row=0, column=0, columnspan=2, pady=(10, 5))

    tk.Label(ventana, text="ID Turno:").grid(row=1, column=0, sticky="w", padx=5)
    id_turno = tk.Entry(ventana)
    id_turno.grid(row=1, column=1, padx=5)

    def cancelar_por_id():
        try:
            mensaje = gestion_turnos_db.cancelar_turno(id_turno.get())
            messagebox.showinfo("Éxito", mensaje)
            ventana.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    tk.Button(ventana, text="Cancelar por ID", command=cancelar_por_id).grid(row=2, column=0, columnspan=2, pady=(5, 15))


    tk.Label(ventana, text="").grid(row=3, column=0)


    tk.Label(ventana, text="Cancelar Turnos por Médico y Rango de Fechas:").grid(row=4, column=0, columnspan=2, pady=(10, 5))

    tk.Label(ventana, text="ID Médico:").grid(row=5, column=0, sticky="w", padx=5)
    tk.Label(ventana, text="Fecha Inicio (YYYY-MM-DD):").grid(row=6, column=0, sticky="w", padx=5)
    tk.Label(ventana, text="Fecha Fin (YYYY-MM-DD):").grid(row=7, column=0, sticky="w", padx=5)

    id_medico = tk.Entry(ventana)
    fecha_inicio = tk.Entry(ventana)
    fecha_fin = tk.Entry(ventana)

    id_medico.grid(row=5, column=1, padx=5)
    fecha_inicio.grid(row=6, column=1, padx=5)
    fecha_fin.grid(row=7, column=1, padx=5)

    def cancelar_por_rango():
        try:
            mensaje = gestion_turnos_db.cancelar_turnos_por_medico_y_fecha(
                id_medico.get(), fecha_inicio.get(), fecha_fin.get()
            )
            messagebox.showinfo("Éxito", mensaje)
            ventana.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    tk.Button(ventana, text="Cancelar por Médico y Fechas", command=cancelar_por_rango).grid(row=8, column=0, columnspan=2, pady=(5, 15))

def actualizar_turno():
    ventana = Toplevel(root)
    ventana.title("Actualizar Turno")


    tk.Label(ventana, text="Buscar Turno por ID:").grid(row=0, column=0, columnspan=2, pady=(10, 5))

    tk.Label(ventana, text="ID Turno:").grid(row=1, column=0, sticky="w", padx=5)
    id_turno = tk.Entry(ventana)
    id_turno.grid(row=1, column=1, padx=5)

    datos_turno = tk.StringVar()
    tk.Label(ventana, textvariable=datos_turno, wraplength=300, justify="left").grid(row=3, column=0, columnspan=2, pady=10)

    def cargar_turno():
        try:
            turno = gestion_turnos_db.ver_turno(id_turno.get())
            if turno:
                datos_turno.set(f"ID Paciente: {turno[0][1]}\nID Doctor: {turno[0][2]}\nFecha: {turno[0][3]}\nHora: {turno[0][4]}\nEstado: {turno[0][5]}")
            else:
                messagebox.showerror("Error", "No se encontró un turno con el ID proporcionado.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    tk.Button(ventana, text="Cargar Turno", command=cargar_turno).grid(row=2, column=0, columnspan=2, pady=(5, 15))


    tk.Label(ventana, text="Actualizar Turno:").grid(row=4, column=0, columnspan=2, pady=(10, 5))

    tk.Label(ventana, text="Nueva Fecha (YYYY-MM-DD):").grid(row=5, column=0, sticky="w", padx=5)
    tk.Label(ventana, text="Nueva Hora (HH:MM:SS):").grid(row=6, column=0, sticky="w", padx=5)
    tk.Label(ventana, text="Nuevo Estado:").grid(row=7, column=0, sticky="w", padx=5)

    nueva_fecha = tk.Entry(ventana)
    nueva_hora = tk.Entry(ventana)
    nuevo_estado = tk.Entry(ventana)

    nueva_fecha.grid(row=5, column=1, padx=5)
    nueva_hora.grid(row=6, column=1, padx=5)
    nuevo_estado.grid(row=7, column=1, padx=5)

    def guardar_cambios():
        try:
            mensaje = gestion_turnos_db.actualizar_turno(
                id_turno.get(),
                nueva_fecha.get(),
                nueva_hora.get(),
                nuevo_estado.get()
            )
            messagebox.showinfo("Éxito", mensaje)
            ventana.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    tk.Button(ventana, text="Guardar Cambios", command=guardar_cambios).grid(row=8, column=0, columnspan=2, pady=(5, 15))


tk.Label(root, text="Pacientes", font=("Arial", 16, "bold")).grid(row=0, column=0, columnspan=2, pady=(10, 0))  
tk.Button(root, text="Buscar Paciente", command=mostrar_busqueda_paciente).grid(row=2, column=0, columnspan=2, pady=5)
tk.Button(root, text="Agregar Paciente", command=agregar_paciente).grid(row=3, column=0, columnspan=2, pady=5)
tk.Button(root, text="Modificar Pacientes", command=modificar_pacientes).grid(row=4, column=0, columnspan=2, pady=5)
tk.Button(root, text="Eliminar Paciente", command=eliminar_paciente).grid(row=5, column=0, columnspan=2, pady=5)

tk.Label(root, text="Doctores", font=("Arial", 16, "bold")).grid(row=0, column=8, columnspan=2, pady=(10, 0))  
tk.Button(root, text="Buscar Doctor", command=mostrar_busqueda_Doctores).grid(row=2, column=8, columnspan=2, pady=5)
tk.Button(root, text="Agregar Doctor", command=agregar_Doctor).grid(row=3, column=8, columnspan=2, pady=5)
tk.Button(root, text="Modificar Doctores", command=modificar_Doctores).grid(row=4, column=8, columnspan=2, pady=5)
tk.Button(root, text="Eliminar Doctor", command=eliminar_doctor).grid(row=5, column=8, columnspan=2, pady=5)

tk.Label(root, text="Turnos", font=("Arial", 16, "bold")).grid(row=0, column=12, columnspan=2, pady=(10, 0))  
tk.Button(root, text="Programar Turno", command=programar_turno).grid(row=2, column=12, columnspan=2, pady=5)
tk.Button(root, text="Ver Turnos", command=ver_turno).grid(row=3, column=12, columnspan=2, pady=5)
tk.Button(root, text="Cancelar Turnos", command=cancelar_turno).grid(row=4, column=12, columnspan=2, pady=5)
tk.Button(root, text="Modificar Turnos", command=actualizar_turno).grid(row=5, column=12, columnspan=2, pady=5)

root.mainloop()

db.desconectar()