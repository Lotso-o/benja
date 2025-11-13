/*

CREATE TABLE Usuario ( 

    Rut VARCHAR(12) PRIMARY KEY, 
    Nombre VARCHAR(100) NOT NULL, 
    Correo VARCHAR(100) UNIQUE NOT NULL 

); 



CREATE TABLE Estudiantes ( 

    Rut VARCHAR(12) PRIMARY KEY, 

    FOREIGN KEY (rut) REFERENCES Usuario(rut) 

        ON DELETE CASCADE ON UPDATE CASCADE 

); 


CREATE TABLE Docentes ( 

    Rut VARCHAR(12) PRIMARY KEY, 

    FOREIGN KEY (rut) REFERENCES Usuario(rut) 

        ON DELETE CASCADE ON UPDATE CASCADE 

); 


CREATE TABLE Administrativo ( 

    Rut VARCHAR(12) PRIMARY KEY, 

    FOREIGN KEY (rut) REFERENCES Usuario(rut) 

        ON DELETE CASCADE ON UPDATE CASCADE 

); 



CREATE TABLE Asignatura ( 

    Id INT PRIMARY KEY AUTO_INCREMENT, -- ID interno de la asignatura 

    Nombre VARCHAR(100) UNIQUE NOT NULL, 
       
    Docente_rut VARCHAR(12), 

    FOREIGN KEY (docente_rut) REFERENCES Docentes(rut) 

        ON DELETE SET NULL ON UPDATE CASCADE 

); 


calificaciones



*/