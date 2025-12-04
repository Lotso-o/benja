CREATE TABLE usuario (
    rut VARCHAR(10) PRIMARY KEY,   
    nombre VARCHAR(45),            
    correoElectronico VARCHAR(30)  
);

CREATE TABLE estudiante (
    id_estudiante INTEGER PRIMARY KEY,    
    rut_usuario VARCHAR(10),              
    matricula VARCHAR(15),                
    FOREIGN KEY (rut_usuario) REFERENCES usuario(rut)
);

CREATE TABLE docente (
    id_docente INTEGER PRIMARY KEY,       
    rut_usuario VARCHAR(10),              
    FOREIGN KEY (rut_usuario) REFERENCES usuario(rut)
);

CREATE TABLE administrativo (
    id_administrativo INTEGER PRIMARY KEY,  
    rut_usuario VARCHAR(10),                
    area VARCHAR(45),                       
    FOREIGN KEY (rut_usuario) REFERENCES usuario(rut)
);

CREATE TABLE asignatura (
    codigo VARCHAR(15) PRIMARY KEY,  
    nombre VARCHAR(45),              
    docente_asociado INTEGER,        
    FOREIGN KEY (docente_asociado) REFERENCES docente(id_docente)
);

CREATE TABLE calificacion (
    id_calificacion INTEGER PRIMARY KEY,    
    valor FLOAT,                             
    asignatura_codigo VARCHAR(15),           
    id_estudiante INTEGER,                  
    FOREIGN KEY (asignatura_codigo) REFERENCES asignatura(codigo),
    FOREIGN KEY (id_estudiante) REFERENCES estudiante(id_estudiante)
);

CREATE TABLE matricula_asignatura (
    id_estudiante INTEGER,                
    codigo_asignatura VARCHAR(15),        
    PRIMARY KEY (id_estudiante, codigo_asignatura), 
    FOREIGN KEY (id_estudiante) REFERENCES estudiante(id_estudiante),  
    FOREIGN KEY (codigo_asignatura) REFERENCES asignatura(codigo)     
);
