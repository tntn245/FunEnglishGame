from flask import request, url_for, redirect, Blueprint
from bson.objectid import ObjectId
import db as app

show_dialog_blueprint = Blueprint('show_dialog_blueprint', __name__)

@show_dialog_blueprint.post('/show_dialog')
def show_dialog():
    showdialog = request.form['form_dialog']
    app.show_Dialog = ObjectId(showdialog)
    return redirect(url_for('index_blueprint.index'))