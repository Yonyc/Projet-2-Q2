CREATE TABLE animaux (
    id INT              NOT NULL,
    famille_id INT     NOT NULL,
    sexe TEXT           NOT NULL,
    presence INT        NOT NULL,
    apprivoise INT      NOT NULL,
    mort_ne INT         NOT NULL,
    decede INT          NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (famille_id) REFERENCES familles(id)
);

CREATE TABLE familles (
    id INT      NOT NULL,
    nom TEXT    NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE types (
    id INT       NOT NULL,
    type TEXT    NOT NULL,
    PRIMARY KEY (id)
);


CREATE TABLE animaux_types (
    animal_id INT           NOT NULL,
    type_id INT             NOT NULL,
    pourcentage REAL        NOT NULL,
    PRIMARY KEY (animal_id, type_id),
    FOREIGN KEY (animal_id) REFERENCES animaux(id),
    FOREIGN KEY (type_id) REFERENCES types(id)
);


CREATE TABLE velages (
    id INT      NOT NULL,
    mere_id INT NOT NULL,
    pere_id INT NOT NULL,
    date TEXT   NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (mere_id) REFERENCES animaux(id),
    FOREIGN KEY (pere_id) REFERENCES animaux(id)
);


CREATE TABLE animaux_velages (
    animal_id INT   NOT NULL,
    velage_id INT   NOT NULL,
    PRIMARY KEY (animal_id, velage_id),
    FOREIGN KEY (animal_id) REFERENCES animaux(id),
    FOREIGN KEY (velage_id) REFERENCES velages(id)
);


CREATE TABLE complications (
    id INT              NOT NULL,
    complication TEXT   NOT NULL,
    PRIMARY KEY (id)
);


CREATE TABLE velages_complications ( 
    velage_id INT       NOT NULL,
    complication_id INT NOT NULL,
    PRIMARY KEY (velage_id, complication_id),
    FOREIGN KEY (velage_id) REFERENCES velages(id),
    FOREIGN KEY (complication_id) REFERENCES complications(id)

);