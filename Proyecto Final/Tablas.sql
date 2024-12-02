use Hospital;

CREATE TABLE IF NOT EXISTS `Pacientes` (
  `id_paciente` INT PRIMARY KEY AUTO_INCREMENT,
  `nombre` VARCHAR(100) NOT NULL,
  `fecha_nacimiento` DATE NOT NULL,
  `historia_clinica` TEXT
);

CREATE TABLE IF NOT EXISTS `Doctores` (
  `id_doctor` INT PRIMARY KEY AUTO_INCREMENT,
  `nombre` VARCHAR(100) NOT NULL,
  `especialidad` VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS `Turnos` (
  `id_turno` INT PRIMARY KEY AUTO_INCREMENT,
  `id_paciente` INT NOT NULL,
  `id_doctor` INT NOT NULL,
  `fecha` DATE NOT NULL,
  `hora` TIME NOT NULL,
  `estado` VARCHAR(50),
  FOREIGN KEY (id_paciente) REFERENCES Pacientes(id_paciente),
  FOREIGN KEY (id_doctor) REFERENCES Doctores(id_doctor) 
);

INSERT INTO Pacientes (id_paciente, nombre, fecha_nacimiento, historia_clinica)
VALUES
(1, 'Juan Perez', '1985-04-12', 'Alergia al polen'),
(2, 'María López', '1990-06-22', 'Hipertensión'),
(3, 'Carlos García', '1982-11-15', 'Asma'),
(4, 'Ana Martínez', '1978-03-30', 'Diabetes tipo 2'),
(5, 'Luis Gómez', '1995-08-19', 'Migrañas'),
(6, 'Sofía Ramírez', '2000-01-12', 'Fractura de brazo'),
(7, 'Miguel Torres', '1988-05-03', 'Problemas cardíacos'),
(8, 'Laura Díaz', '1992-09-10', 'Artritis'),
(9, 'Jorge Fernández', '1983-07-21', 'Sin antecedentes'),
(10, 'Carmen Castillo', '1975-12-05', 'Cáncer en remisión');

INSERT INTO Doctores (id_doctor, nombre, especialidad)
VALUES
(1, 'Dr. Roberto Sánchez', 'Cardiología'),
(2, 'Dra. Lucía Fernández', 'Neurología'),
(3, 'Dr. Antonio Ruiz', 'Pediatría'),
(4, 'Dra. Elena Gómez', 'Ginecología'),
(5, 'Dr. Javier Morales', 'Dermatología'),
(6, 'Dra. Clara Ortega', 'Oftalmología'),
(7, 'Dr. Andrés Méndez', 'Oncología'),
(8, 'Dra. Verónica Pérez', 'Psiquiatría'),
(9, 'Dr. Fernando Soto', 'Traumatología'),
(10, 'Dra. Gabriela López', 'Endocrinología');

INSERT INTO Turnos (id_paciente, id_doctor, fecha, hora, estado)
VALUES
(1, 2, '2024-12-01', '10:00:00', 'Programado'),
(2, 3, '2024-12-02', '14:30:00', 'Programado'),
(3, 1, '2024-12-03', '09:15:00', 'Programado'),
(4, 5, '2024-12-04', '08:00:00', 'Programado'),
(5, 4, '2024-12-05', '11:00:00', 'Programado'),
(6, 3, '2024-12-06', '13:30:00', 'Programado'),
(7, 2, '2024-12-07', '15:45:00', 'Programado'),
(8, 1, '2024-12-08', '10:30:00', 'Programado'),
(9, 4, '2024-12-09', '12:00:00', 'Programado'),
(10, 5, '2024-12-10', '14:00:00', 'Programado');


SELECT * FROM Pacientes;
SELECT * FROM Doctores;
SELECT * FROM Turnos;