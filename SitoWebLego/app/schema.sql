CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);


CREATE TABLE lego (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    set_number TEXT NOT NULL,
    pieces INTEGER,
    year INTEGER,
    description TEXT,
    image TEXT,
    owner_id INTEGER NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    price REAL,
    color TEXT,
    is_minifigure BOOLEAN,
    is_botanica BOOLEAN,
    FOREIGN KEY (owner_id) REFERENCES user(id)
);
