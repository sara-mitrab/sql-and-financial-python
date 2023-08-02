-- Table "actions"

CREATE DATABASE python; 
USE python;
CREATE TABLE actions (
  id INTEGER PRIMARY KEY,
  nom TEXT,
  prix REAL,
  quantite INTEGER
);

-- Table "obligations"
CREATE TABLE obligations (
  id INTEGER PRIMARY KEY,
  nom TEXT,
  prix REAL,
  taux_interet REAL
);

CREATE TABLE operations_sur_action (
  action_id INTEGER PRIMARY KEY,
  date DATE,
  montant REAL,
  FOREIGN KEY (action_id) REFERENCES actions (id)
);


CREATE TABLE operations_sur_obligation (
  obligation_id INTEGER PRIMARY KEY,
  date DATE,
  montant REAL,
  FOREIGN KEY (obligation_id) REFERENCES obligations (id)
);


INSERT INTO actions (id,nom, prix, quantite) VALUES
    (1,'Action B', 15.2, 200),
    (2,'Action C', 12.8, 150),
    (3,'Action D', 8.5, 300);


INSERT INTO obligations (id,nom, prix, taux_interet) VALUES
    (1,'Obligation C', 600, 0.03),
    (2,'Obligation D', 550, 0.02),
    (3,'Obligation E', 700, 0.04),
    (4, 'obligation S', 8000, 3.4);


INSERT INTO operations_sur_action (action_id, date, montant) VALUES
    (1, '2023-07-10', 1500),
    (2, '2023-07-11', 2000),
    (3, '2023-07-12', 1000);


INSERT INTO operations_sur_obligation (obligation_id, date, montant) VALUES
    (1, '2023-07-11', 500),
    (2, '2023-07-12', 1000),
    (3, '2023-07-13', 750);
