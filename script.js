document.addEventListener("DOMContentLoaded", () => {
    const actionList = document.getElementById('actionList');
    const obligationList = document.getElementById('obligationList');
    const showActionsLink = document.getElementById('showActions');
    const showObligationsLink = document.getElementById('showObligations');

    showActionsLink.addEventListener('click', (event) => {
        event.preventDefault();
        fetch('/actions')
            .then(response => response.json())
            .then(data => {
                actionList.innerHTML = data.map(action => `<li>Nom: ${action.nom}, Prix: <span class="price">${action.prix}</span></li>`).join('');
                actionList.classList.remove('hidden');
                obligationList.classList.add('hidden');
            });
    });

    showObligationsLink.addEventListener('click', (event) => {
        event.preventDefault();
        fetch('/obligations')
            .then(response => response.json())
            .then(data => {
                obligationList.innerHTML = data.map(obligation => `<li>Nom: ${obligation.nom}, Prix: <span class="price">${obligation.prix}</span>, Taux d'intérêt: ${obligation.taux_interet}</li>`).join('');
                obligationList.classList.remove('hidden');
                actionList.classList.add('hidden');
            });
    });
});

