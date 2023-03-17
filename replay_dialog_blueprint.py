from flask import request, url_for, redirect, Blueprint
from bson.objectid import ObjectId
from datetime import datetime
import time
import db as app

replay_dialog_blueprint = Blueprint('replay_dialog_blueprint', __name__)

@replay_dialog_blueprint.post('/replay_dialog')
def replay_dialog():
    replay_dialog = request.form['form_dialog']
    dialog = list(app.Dialog.find({'_id':ObjectId(replay_dialog)}))
    sentences = list(app.EnglishSentence.find({'DialogId':ObjectId(replay_dialog),'CreatedDate':{"$gte":(dialog[0]['ModifiedDate'])}}))
    app.Dialog.update_one({"_id": ObjectId(replay_dialog)},{"$set":{"ModifiedDate":datetime.now()}})

    for i in sentences:
        # randomName = list(app.Users.aggregate([{ '$match': {'Online': True}},{'$sample': {'size': 1 }}]))
        sentence={'ReceiverName': '', 'Sentence': i['Sentence'], 'Seen': False, 'TimeStamp': '', 'Sent': False, 'CreatedBy': '', 'CreatedDate': datetime.now(), 'ModifiedBy':'', 'ModifiedDate': datetime.now(), 'DialogId':ObjectId(replay_dialog)}
        app.EnglishSentence.insert_one(sentence)
        time.sleep(0.01)
    return redirect(url_for('index_blueprint.index'))