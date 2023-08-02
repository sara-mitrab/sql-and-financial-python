from peewee import *

# Définir la connexion à la base de données
db = MySQLDatabase('python', host='localhost', user='root', password='password')

class Actions(Model):
    id = AutoField()
    nom = CharField()
    prix = FloatField()
    quantite = IntegerField()

    class Meta:
        database = db
        table_name = 'actions'

class Obligations(Model):
    id = AutoField()
    nom = CharField()
    prix = FloatField()
    taux_interet = FloatField()

    class Meta:
        database = db
        table_name = 'obligations'


class OperationsSurAction(Model):
    action_id = ForeignKeyField(Actions, primary_key=True, on_delete='CASCADE')  # Add on_delete='CASCADE'
    date = DateField()
    montant = FloatField()

    class Meta:
        database = db
        table_name = 'operations_sur_action'

class OperationsSurObligation(Model):
    obligation_id = ForeignKeyField(Obligations, primary_key=True)
    date = DateField()
    montant = FloatField()

    class Meta:
        database = db
        table_name = 'operations_sur_obligation'


db.connect()

# Sélection de toutes les actions
actions = Actions.select()
print("voici toutes les actions \t")
for action in actions:
    print(action.nom, action.prix)

# Sélection des obligations avec un taux d'intérêt supérieur à 3%
obligations = Obligations.select().where(Obligations.taux_interet > 3)
print("voici toutes les obligations avec un taux coupon supérieure à 3%")
for obligation in obligations:
    print(obligation.nom, obligation.prix, obligation.taux_interet)

# Sélection des opérations sur actions effectuées après une certaine date
import datetime

date_limite = datetime.date(2022, 1, 1)
operations_actions = OperationsSurAction.select().where(OperationsSurAction.date > date_limite)
for operation in operations_actions:
    print(operation.action_id.nom, operation.montant, operation.date)

