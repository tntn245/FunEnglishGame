from flask import url_for, redirect, Blueprint
from bson.objectid import ObjectId
import db as app

disable_blueprint = Blueprint('disable_blueprint', __name__)

@disable_blueprint.post('/disable/<id>/')
def disable(id):
    user = list(app.Users.find({"_id": ObjectId(id)}))
    if(user[0]['Online']):
        app.Users.update_one({"_id": ObjectId(id)},{"$set":{"Online":False}})
        return redirect(url_for('index_blueprint.index'))

    app.Users.update_one({"_id": ObjectId(id)},{"$set":{"Online":True}})
    return redirect(url_for('index_blueprint.index'))