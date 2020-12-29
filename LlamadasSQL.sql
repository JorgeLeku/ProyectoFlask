ALTER TABLE Usuarios ADD
  id INTEGER PRIMARY KEY,
 ADD nombre VARCHAR,
 ADD creacion DATE,
 ADD direccion VARCHAR,
 ADD email VARCHAR NOT NULL,
 ADD numero INTEGER


CREATE TABLE pedidos (
	id VARCHAR,
	id_usuario INTEGER,
	estado VARCHAR,
	fechaCreacion DATE,
	FOREIGN KEY (id_usuario) REFERENCES usuarios (id)
);

CREATE TABLE productos (
id INTEGER PRIMARY KEY,
nombre VARCHAR,
categoria VARCHAR,
precio DECIMAL,
ubicacion VARCHAR
);

CREATE TABLE pedido_productos (
id INTEGER PRIMARY KEY,
id_productos INTEGER,
id_pedidos INTEGER,
cantidad INTEGER,
FOREIGN KEY (id_productos) REFERENCES productos (id),
FOREIGN KEY (id_pedidos) REFERENCES pedidos (id)
);