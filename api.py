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

if __name__ == "__main__":
    app.run(port=8000)

