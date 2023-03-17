from flask import url_for, redirect, Blueprint
from bson.objectid import ObjectId
import db as app

send_blueprint = Blueprint('send_blueprint', __name__)

@send_blueprint.post('/get_row/<id>/')
def get_row(id):
    if(app.EnglishSentence.find_one({"_id": ObjectId(id), "ReceiverName":""})):
        sentences = list(app.EnglishSentence.find({"ReceiverName":""}))
        for i in sentences:
            randomName = list(app.Users.aggregate([{ '$match': {'Online': True}},{'$sample': {'size': 1 }}]))
            app.EnglishSentence.update_one({"ReceiverName":""},{"$set":{"ReceiverName":randomName[0]['PCName']}})
    else:
        app.EnglishSentence.update_one({"_id": ObjectId(id)},{"$set":{"Sent":True}})
        app.EnglishSentence.update_one({"_id": ObjectId(id)},{"$set":{"Seen":False}})
    return redirect(url_for('index_blueprint.index'))