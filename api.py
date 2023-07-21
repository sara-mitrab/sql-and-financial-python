from flask import Flask, jsonify
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
    obligations = Obligations.select().where(Obligations.taux_interet > 3)
    obligation_list = [{'nom': obligation.nom, 'prix': obligation.prix, 'taux_interet': obligation.taux_interet} for obligation in obligations]
    return jsonify(obligation_list)

# Route pour créer une nouvelle action
@app.route('/actions', methods=['POST'])
def create_action():
    data = request.json
    action = Actions.create(nom=data['nom'], prix=data['prix'], quantite=data['quantite'])
    return jsonify(model_to_dict(action))

# Route to update an existing action
@app.route('/actions/<int:action_id>', methods=['PUT'])
def update_action(action_id):
    data = request.json
    try:
        action = Actions.get(Actions.id == action_id)
        action.nom = data['nom']
        action.prix = data['prix']
        action.quantite = data['quantite']
        action.save()
        return jsonify(model_to_dict(action))
    except Actions.DoesNotExist:
        return jsonify({'error': 'Action not found'}), 404

# Route to delete an action
@app.route('/actions/<int:action_id>', methods=['DELETE'])
def delete_action(action_id):
    try:
        action = Actions.get(Actions.id == action_id)
        action.delete_instance()
        return jsonify({'message': 'Action deleted successfully'})
    except Actions.DoesNotExist:
        return jsonify({'error': 'Action not found'}), 404


if __name__ == "__main__":
    app.run(port=9000)

