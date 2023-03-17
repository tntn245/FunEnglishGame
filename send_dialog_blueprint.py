from flask import url_for, redirect, Blueprint
from bson.objectid import ObjectId
from datetime import datetime
from dialogcontent import DialogContentDTO
import db as app

send_dialog_blueprint = Blueprint('send_dialog_blueprint', __name__)

@send_dialog_blueprint.post('/send_dialog')
def send_dialog():
    dialog_find=list(app.Dialog.find().sort("ModifiedDate", -1).limit(1))            
    randomName = list(app.Users.aggregate([{ '$match': {'Online': True}},{'$sample': {'size': 1 }}]))
    all_sentences = DialogContentDTO(ObjectId(dialog_find[0]['_id']),randomName[0]['PCName'],False,'',datetime.now(),'',datetime.now())
    app.DialogContentNotification.insert_one(all_sentences.__dict__)
    return redirect(url_for('index_blueprint.index'))