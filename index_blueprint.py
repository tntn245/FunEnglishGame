from flask import render_template, request, url_for, redirect, Blueprint
from bson.objectid import ObjectId
import db as app

index_blueprint = Blueprint('index_blueprint', __name__)

@index_blueprint.route('/')
def index():
    if request.method=='POST':
        return redirect(url_for('index'))

    all_Dialog = list(app.Dialog.find())
    all_Dialog_reverse = reversed(all_Dialog)
    all_EnglishSentence = list(app.EnglishSentence.find())
    all_Users = list(app.Users.find())
    all_DialogContentNotification = list(app.DialogContentNotification.find())

    all_EnglishSentence_reverse=list(app.EnglishSentence.find().sort("CreatedDate", -1))
    current_dialog = list(app.Dialog.find({"_id": ObjectId(app.show_Dialog)}))
    all_sentences = list(app.EnglishSentence.find({'DialogId':ObjectId(app.show_Dialog), "CreatedDate":{"$gte":(current_dialog[0]['ModifiedDate'])}}))
    all_user_online = list(app.Users.find({"Online":True}))

    return render_template('index.html',
    Dialog=all_Dialog, Users=all_Users, EnglishSentence=all_EnglishSentence, DialogContentNotification=all_DialogContentNotification,
    Dialog_reverse=all_Dialog_reverse, EnglishSentence_reverse=all_EnglishSentence_reverse,
    New_Dialog=app.dialog_find, show_Dialog=app.show_Dialog,
    Sentences_of_Dialog = all_sentences, Users_online = all_user_online)