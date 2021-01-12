CREATE TABLE usuarios (
	id SERIAL PRIMARY KEY,
	nombre VARCHAR,
	direccion VARCHAR,
	email VARCHAR NOT NULL,
	numero INTEGER,
	password VARCHAR,
);
CREATE TABLE pedidos (
	id SERIAL PRIMARY KEY,
	id_usuario INTEGER,
	id_estado INTEGER,
	id_productos INTEGER,
	fechaCreacion DATE,
	FOREIGN KEY (id_productos) REFERENCES pedido_productos (id),
	FOREIGN KEY (id_usuario) REFERENCES usuarios (id),
	FOREIGN KEY (id_estado) REFERENCES estado (id)
);

CREATE TABLE productos (
	id SERIAL PRIMARY KEY,
	id_categoria INTEGER,
	id_ubicacion INTEGER,
	nombre VARCHAR,
	precio DECIMAL,
	cantidad INTEGER,
	FOREIGN KEY (id_ubicacion) REFERENCES ubicacion (id),
	FOREIGN KEY (id_categoria) REFERENCES categoria (id)
);

CREATE TABLE pedido_productos (
	id SERIAL PRIMARY KEY,
	id_productos INTEGER,
	id_pedidos INTEGER,
	cantidad INTEGER,
	FOREIGN KEY (id_productos) REFERENCES productos (id),
	FOREIGN KEY (id_pedidos) REFERENCES pedidos (id)
);

CREATE TABLE ubicacion (
	id SERIAL PRIMARY KEY,
	ciudad VARCHAR,
);

CREATE TABLE estado (
	id SERIAL PRIMARY KEY,
	estado VARCHAR,
);

CREATE TABLE categoria (
	id SERIAL PRIMARY KEY,
	categoria VARCHAR,
);

