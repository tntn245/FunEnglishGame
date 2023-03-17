from flask import url_for, redirect, Blueprint
from bson.objectid import ObjectId
import db as app

skip_blueprint = Blueprint('skip_blueprint', __name__)

@skip_blueprint.post('/skip/<id>/')
def skip(id):
    app.EnglishSentence.update_one({"_id": ObjectId(id)},{"$set":{"Sent":True}})
    app.EnglishSentence.update_one({"_id": ObjectId(id)},{"$set":{"Seen":True}})
    return redirect(url_for('index_blueprint.index')) 