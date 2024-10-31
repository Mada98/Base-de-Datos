CREATE TABLE Usuarios (
    Id INT PRIMARY KEY AUTO_INCREMENT,
    NombreUsuario VARCHAR(50) NOT NULL,
    Email VARCHAR(100) NOT NULL,
    FechaRegistro DATE NOT NULL,
    Estado VARCHAR(20) NOT NULL
);

INSERT INTO Usuarios (NombreUsuario, Email, FechaRegistro, Estado) VALUES
('usuario1', 'usuario1@example.com', '2022-01-01', 'Activo'),     
('usuario2', 'usuario2@example.com', '2023-01-05', 'Activo'),      
('usuario3', 'usuario3@example.com', '2023-01-10', 'Inactivo'),    
('usuario5', 'usuario5@example.com', '2022-12-15', 'Pendiente'),    
('usuario6', 'usuario6@example.com', '2023-02-25', 'Activo'),     
('usuario7', 'usuario7@example.com', '2021-06-01', 'Inactivo'),    
('usuario8', 'usuario8@example.com', '2022-05-05', 'Activo'),      
('usuario9', 'usuario9@example.com', '2023-02-10', 'Pendiente'),   
('usuario10', 'usuario10@example.com', '2022-07-15', 'Activo'),    
('usuario11', 'usuario11@example.com', '2021-11-01', 'Inactivo'),   
('usuario12', 'usuario12@example.com', '2023-01-20', 'Activo'),   
('usuario13', 'usuario13@example.com', '2023-03-15', 'Pendiente'),  
('usuario14', 'usuario14@example.com', '2020-05-05', 'Activo'),    
('usuario15', 'usuario15@example.com', '2022-09-10', 'Inactivo'),  
('usuario16', 'usuario16@example.com', '2023-04-15', 'Activo'),    
('usuario17', 'usuario17@example.com', '2023-03-20', 'Pendiente'),   
('usuario18', 'usuario18@example.com', '2023-05-01', 'Activo'),      
('usuario19', 'usuario19@example.com', '2023-02-20', 'Inactivo'),    
('usuario20', 'usuario20@example.com', '2021-10-10', 'Activo');      

DELIMITER//
create procedure ValidarUsuarios()
begin
	declare terminado INT default false;
	declare Id INT;
	declare FechaRegistro date;
	declare Estado varchar(20);
	
	declare _Cursor cursor for
	select Id, FechaRegistro, Estado from Usuarios;

	declare continue handler for not found set terminado = true;

	open _Cursor;

	read_loop: loop
		fetch _Cursor into Id, FechaRegistro, Estado;
		if terminado then
			leave read_loop;
		end if;
	
		if Estado = "Inactivo" and datediff(CURDATE(), FechaRegistro) > 7 then
			UPDATE Usuarios SET Estado = 'Inactivo' WHERE Id = Id;
        ELSEIF estado = 'Activo' AND DATEDIFF(CURDATE(), FechaRegistro) > 365 THEN
			-- notificacion
        END IF;
  END LOOP;
 CLOSE _Cursor;
END 
	
DELIMITER;	




