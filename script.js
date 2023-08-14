// Code JavaScript pour rendre les signes d'euros aléatoires et afficher les données dans les tableaux

const euroSigns = document.querySelectorAll('.random-euros span');
const actionTable = document.getElementById('action-table').getElementsByTagName('tbody')[0];
const obligationTable = document.getElementById('obligation-table').getElementsByTagName('tbody')[0];

// Fonction pour générer une position aléatoire
function randomPosition() {
    return {
        top: Math.random() * window.innerHeight,
        left: Math.random() * window.innerWidth,
    };
}

// Appliquer une position aléatoire aux signes d'euros
euroSigns.forEach(sign => {
    const position = randomPosition();
    sign.style.top = `${position.top}px`;
    sign.style.left = `${position.left}px`;
});

// Exemple de données d'actions et d'obligations (peut être remplacé par les données réelles)
const actionsData = [
    { nom: 'Action 1', prix: 100 },
    { nom: 'Action 2', prix: 150 },
    // ...
];

const obligationsData = [
    { nom: 'Obligation 1', prix: 1000, taux_interet: 5 },
    { nom: 'Obligation 2', prix: 1200, taux_interet: 4 },
    // ...
];

// Fonction pour afficher les données dans les tableaux
function populateTable(table, data) {
    table.innerHTML = '';
    data.forEach(item => {
        const row = table.insertRow();
        const cell1 = row.insertCell(0);
        const cell2 = row.insertCell(1);
        const cell3 = row.insertCell(2);

        cell1.innerHTML = item.nom;
        cell2.innerHTML = item.prix;
        if (item.taux_interet) {
            cell3.innerHTML = item.taux_interet;
        }
    });
}

// Appeler la fonction pour afficher les données dans les tableaux
populateTable(actionTable, actionsData);
populateTable(obligationTable, obligationsData);
