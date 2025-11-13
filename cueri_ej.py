

def create_schema():

    (
        CREATE TABLE
          Usuario ( 
    Rut VARCHAR(12) PRIMARY KEY, 
    Nombre VARCHAR(100) NOT NULL, 
    Correo VARCHAR(100) UNIQUE NOT NULL ); 
    ),

    (
        CREATE TABLE Estudiantes ( 

    Rut VARCHAR(12) PRIMARY KEY, 

    FOREIGN KEY (rut) REFERENCES Usuario(rut) 

        ON DELETE CASCADE ON UPDATE CASCADE 
        ); 

    ),

    (
        CREATE TABLE Docentes ( 

    Rut VARCHAR(12) PRIMARY KEY, 

    FOREIGN KEY (rut) REFERENCES Usuario(rut) 

        ON DELETE CASCADE ON UPDATE CASCADE 
        
        ); 
    ),

    (
        CREATE TABLE Administrativo ( 

    Rut VARCHAR(12) PRIMARY KEY, 

    FOREIGN KEY (rut) REFERENCES Usuario(rut) 

        ON DELETE CASCADE ON UPDATE CASCADE 
        ); 
    ),

    (
        CREATE TABLE Asignatura ( 

    Id INT PRIMARY KEY AUTO_INCREMENT, -- ID interno de la asignatura 

    Nombre VARCHAR(100) UNIQUE NOT NULL, 
       
    Docente_rut VARCHAR(12), 

    FOREIGN KEY (docente_rut) REFERENCES Docentes(rut) 

        ON DELETE SET NULL ON UPDATE CASCADE 
        ); 

    ),

    (
        CREATE TABLE Calificaciones ( 

    Id INT PRIMARY KEY AUTO_INCREMENT, 

    Asignatura_id INT NOT NULL, 

    Estudiante_rut VARCHAR(12) NOT NULL, 

    Calificacion FLOAT NOT NULL, 

    Fecha DATE NOT NULL, 


    FOREIGN KEY (asignatura_id) REFERENCES Asignatura(id) 

        ON DELETE RESTRICT ON UPDATE CASCADE, 


    FOREIGN KEY (estudiante_rut) REFERENCES Estudiantes(rut) 

        ON DELETE CASCADE ON UPDATE CASCADE, 


    UNIQUE KEY (asignatura_id, estudiante_rut, fecha)  

); 
    )


for