
CREATE DATABASE projet;
USE projet;


CREATE TABLE Actions (
  ID INT PRIMARY KEY,
  Symbole VARCHAR(10),
  Nom VARCHAR(255),
  Description VARCHAR(255),
  Secteur VARCHAR(50),
  Pays VARCHAR(50),
  ValeurNominale DECIMAL(10,2),
  ValeurMarchande DECIMAL(10,2),
  Dividende DECIMAL(10,2),
  NombreActions INT,
  Proprietaire VARCHAR(100),
  DateEmission DATE
);


CREATE TABLE OperationsAction (
  ID INT PRIMARY KEY,
  ActionID INT,
  TypeOperation VARCHAR(50),
  Quantite INT,
  Prix DECIMAL(10,2),
  DateOperation DATE,
  FOREIGN KEY (ActionID) REFERENCES Actions(ID)
);


CREATE TABLE Obligations (
  ID INT PRIMARY KEY,
  Symbole VARCHAR(10),
  Nom VARCHAR(255),
  Description VARCHAR(255),
  Pays VARCHAR(50),
  Devise VARCHAR(10),
  MontantNominal DECIMAL(10,2),
  TauxInteret DECIMAL(5,2),
  DateEmission DATE,
  DateEcheance DATE,
  Proprietaire VARCHAR(100)
);


CREATE TABLE OperationsObligation (
  ID INT PRIMARY KEY,
  ObligationID INT,
  TypeOperation VARCHAR(50),
  Montant DECIMAL(10,2),
  DateOperation DATE,
  FOREIGN KEY (ObligationID) REFERENCES Obligations(ID)
);


INSERT INTO Actions (ID, Symbole, Nom, Description, Secteur, Pays, ValeurNominale, ValeurMarchande, Dividende, NombreActions, Proprietaire, DateEmission)
VALUES (1, 'AAPL', 'Apple Inc.', 'Entreprise technologique', 'Technologie', 'États-Unis', 100.00, 150.00, 2.00, 1000000, 'John Doe', '2022-01-01');

INSERT INTO OperationsAction (ID, ActionID, TypeOperation, Quantite, Prix, DateOperation)
VALUES (1, 1, 'Achat', 100, 140.00, '2022-02-15');

INSERT INTO Obligations (ID, Symbole, Nom, Description, Pays, Devise, MontantNominal, TauxInteret, DateEmission, DateEcheance, Proprietaire)
VALUES (1, 'GOVT2025', 'Government Bond 2025', 'Obligation gouvernementale', 'États-Unis', 'USD', 1000.00, 3.50, '2021-01-01', '2025-01-01', 'Jane Smith');

INSERT INTO OperationsObligation (ID, ObligationID, TypeOperation, Montant, DateOperation)
VALUES (1, 1, 'Achat', 500.00, '2022-03-20');
