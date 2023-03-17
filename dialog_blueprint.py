from flask import render_template, request, url_for, redirect, Blueprint
from datetime import datetime
from dialog import DialogDTO
import db as app

dialog_blueprint = Blueprint('dialog_blueprint', __name__)

@dialog_blueprint.route('/new_dialog', methods=('GET', 'POST'))
def new_dialog():
    if request.method=='POST':
        new_dialog = request.form['new_dialog']
        dialog = DialogDTO(new_dialog,'',datetime.now(),'',datetime.now())
        app.Dialog.insert_one(dialog.__dict__)
        app.dialog_find = list(app.Dialog.find().sort("ModifiedDate", -1).limit(1))
        app.show_Dialog = app.dialog_find[0]['_id']
        return redirect(url_for('index_blueprint.index'))

    all_Dialog = list(app.Dialog.find())
    return render_template('index.html', Dialog=all_Dialog)