**Proyecto 3: Sistema de Gestión de Hospital**

### Paso 1: Determinar las Dependencias Funcionales (DFs)

1. id_paciente -> nombre, fecha_nacimiento, historia_clinica: Como cada paciente tiene sus propios datos personales y medicos, se podria decir que `nombre`, `fecha_nacimiento`, `historia_clinica` dependen de `id_paciente`.

2. id_doctor -> nombre, especialidad: Cada `id_doctor` está definido con un nombre y especialidad únicos, por lo tanto `nombre` y `especialidad` dependen de `id_doctor`.

3. id_turno -> id_paciente, id_medico, fecha, hora, estado: Cada `id_turno` se identifica de manera única y cada turno tiene un paciente, un médico, una fecha y una hora asignada, por lo que `id_paciente`, `id_doctor`, `fecha`, `hora` y `estado` dependen de `id_turno`.


### Paso 2: Determinar las Claves Candidatas

En este caso, podemos ver que:

- La combinación de **`id_paciente`, `id_doctor`, y `id_turno`** es suficiente para identificar de forma única cada registro en la tabla, ya que:
  
- `id_paciente` identifica el paciente.
- `id_doctor` identifica el doctor.
- `id_turno` identifica el turno.

Por lo tanto, las **claves candidatas** son:

- (`id_paciente`, `id_doctor`, `id_turno`)

Esta combinación asegura que cada registro en la tabla sea único y no haya duplicados.

### Paso 3: Diseño en Tercera Forma Normal (3FN)

El diseño en 3FN sería el siguiente:

1. **Tabla `Pacientes`**
   - `id_paciente` (Clave primaria que referencia al `Paciente`)
   - `nombre` 
   - `fecha_nacimineto` 

2. **Tabla `Doctores`**
   - `id_doctor` (Clave primaria que referencia al `Doctor`)
   - `nombre
   - `especialidad`

3. **Tabla `Turnos`**
   - `id_turno` (Clave primaria que referencia al `Turno`)
   - `id_paciente` (Clave foránea que referencia a `Pacientes`)
   - `id_doctor` (Clave foránea que referencia a `Doctores`)
   - `fecha`
   - `hora`
   - `estado`
