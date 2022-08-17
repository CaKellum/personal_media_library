CREATE TABLE formats (
    format_id INTEGER PRIMARY KEY AUTOINCREMENT,
    format_name TEXT NOT NULL
);

CREATE TABLE media (
    item_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    format_id INTEGER NOT NULL,
    shared_disc BOOL DEFAULT False,
    run_time INTEGER,
    FOREIGN KEY(format_id) REFERENCES formats(format_id)
);

INSERT INTO formats (format_name)
VALUES ("Playstation"); 
INSERT INTO formats (format_name)
VALUES ("Playstation2");
INSERT INTO formats (format_name)
VALUES ("Playstation3");
INSERT INTO formats (format_name)
VALUES ("Playstation4");
INSERT INTO formats (format_name)
VALUES ("Playstation5");

INSERT INTO formats (format_name)
VALUES ("Wii");
INSERT INTO formats (format_name)
VALUES ("GameCube");
INSERT INTO formats (format_name)
VALUES ("N64");
INSERT INTO formats (format_name)
VALUES ("SNES");
INSERT INTO formats (format_name)
VALUES ("NES");
INSERT INTO formats (format_name)
VALUES ("GameBoy");
INSERT INTO formats (format_name)
VALUES ("GameBoy Advanced");
INSERT INTO formats (format_name)
VALUES ("GameBoy Color");
INSERT INTO formats (format_name)
VALUES ("DS");
INSERT INTO formats (format_name)
VALUES ("3DS");
INSERT INTO formats (format_name)
VALUES ("Switch");

INSERT INTO formats (format_name)
VALUES ("Sega Genesis");

INSERT INTO formats (format_name)
VALUES ("PC");

INSERT INTO formats (format_name)
VALUES ("Vynil");
INSERT INTO formats (format_name)
VALUES ("Cassette");
INSERT INTO formats (format_name)
VALUES ("CD");

INSERT INTO formats (format_name)
VALUES ("VHS");
INSERT INTO formats (format_name)
VALUES ("DVD");
INSERT INTO formats (format_name)
VALUES ("Blu-ray");