 from flask import Flask, jsonify, render_template, request
from peewee import *
from model import Actions, Obligations, OperationsSurAction, OperationsSurObligation

app = Flask(__name__)

# Route to retrieve all actions
@app.route('/actions', methods=['GET'])
def get_actions():
    actions = Actions.select()
    action_list = [{'nom': action.nom, 'prix': action.prix} for action in actions]
    return jsonify(action_list)

# Route to retrieve obligations with interest rate greater than 3%
@app.route('/obligations', methods=['GET'])
def get_obligations():
    obligations = Obligations.select()
    obligation_list = [{'nom': obligation.nom, 'prix': obligation.prix, 'taux_interet': obligation.taux_interet} for obligation in obligations]
    return jsonify(obligation_list)

# Route to display the homepage with all actions and obligations
@app.route('/', methods=['GET'])
def index():
    actions = Actions.select()
    obligations = Obligations.select().where(Obligations.taux_interet > 3)
    return render_template('index.html', actions=actions, obligations=obligations)

# Route to add a new action
@app.route('/actions', methods=['POST'])
def add_action():
    data = request.json

    if "nom" in data and "prix" in data and "quantite" in data:
        nouvelle_action = {
            "nom": data["nom"],
            "prix": data["prix"],
            "quantite": data["quantite"]
        }
        # You can save the nouvelle_action to your database or perform any other required action here.

        return jsonify({"message": "Nouvelle action ajoutée avec succès !"}), 201
    else:
        return jsonify({"message": "Les données envoyées sont incomplètes."}), 400

# Route to delete an existing action
@app.route('/actions/<int:action_id>', methods=['DELETE'])
def delete_action(action_id):
    try:
        action = Actions.get(Actions.id == action_id)
    except Actions.DoesNotExist:
        return jsonify({"message": "L'action avec l'ID spécifié n'existe pas."}), 404

    try:
        action.delete_instance()
        print("Action deleted:", action.id)
        return jsonify({"message": "Action supprimée avec succès !"}), 200
    except Exception as e:
        print("Error deleting action:", str(e))
        return jsonify({"message": "Une erreur s'est produite lors de la suppression de l'action.", "error": str(e)}), 500

@app.route('/test', methods=['GET', 'POST'])
def test():
    return jsonify({"message": "Test route works!"})

if __name__ == "__main__":
    app.run(port=9000)
