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
  deal_id_ac int auto_increment primary key,
  action_id int,
  date DATE,
  montant REAL,
  FOREIGN KEY (action_id) REFERENCES actions (id)
);


CREATE TABLE operations_sur_obligation (
  deal_id_ob int auto_increment primary key,
  obligation_id INTEGER ,
  date DATE,
  montant REAL,
  FOREIGN KEY (obligation_id) REFERENCES obligations (id)
);


INSERT INTO actions (id,nom, prix, quantite) VALUES
    (134,'Action B', 15.2, 200),
    (256,'Action C', 12.8, 150),
    (387,'Action D', 8.5, 300);


INSERT INTO obligations (id,nom, prix, taux_interet) VALUES
    (157,'Obligation C', 600, 0.03),
    (298,'Obligation D', 550, 0.02),
    (312,'Obligation E', 700, 0.04),
    (498, 'obligation S', 8000, 3.4);


INSERT INTO operations_sur_action (action_id, date, montant) VALUES
    (134, '2023-07-10', 1500),
    (256, '2023-07-11', 2000),
    (387, '2023-07-12', 1000);


INSERT INTO operations_sur_obligation (obligation_id, date, montant) VALUES
    (157, '2023-07-11', 500),
    (298, '2023-07-12', 1000),
    (312, '2023-07-13', 750);
