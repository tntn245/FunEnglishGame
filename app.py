from operator import truediv
from flask import Flask, render_template, request, url_for, redirect
from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import datetime


app = Flask(__name__)

client = MongoClient('mongodb://localhost:27017/')
test = MongoClient('mongodb://root:123@103.116.106.153:2718/?authMechanism=DEFAULT')


db = client.flask_db
feg = db.feg
todos = db.todos
user = db.user

dbo = test.FunEnglishGamePrj
Dialog = dbo.Dialog
Users = dbo.Users
EnglishSentence = dbo.EnglishSentence
DialogContentNotification = dbo.DialogContentNotification


@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method=='POST':
        sentences = request.form['sentences']
        new_dialog = request.form['new_dialog']
        new = request.form['new']
        feg.insert_one({'sentences': sentences, 'dialog': new_dialog, 'new': new})
        return redirect(url_for('index'))

    all_feg = list(feg.find())
    all_todos = list(todos.find())
    all_user = list(user.find())
    all_Dialog = list(Dialog.find())
    all_Dialog_reverse = reversed(all_Dialog)
    all_Users = list(Users.find())
    all_EnglishSentence = list(EnglishSentence.find())
    all_DialogContentNotification = list(DialogContentNotification.find())

    dialog_find=feg.find().sort("Date", -1).limit(1)

    return render_template('index.html', feg=all_feg, todos=all_todos, user=all_user,
    Dialog=all_Dialog, Users=all_Users, EnglishSentence=all_EnglishSentence, DialogContentNotification=all_DialogContentNotification,
    Dialog_reverse=all_Dialog_reverse, New_Dialog=dialog_find)

@app.route('/new_dialog', methods=('GET', 'POST'))
def new_dialog():
    if request.method=='POST':
        new_dialog = request.form['new_dialog']
        dialog ={'Name': new_dialog,'CreatedBy': '', 'Date': datetime.now(), 'ModifiedBy': '', 'ModifiedDate': datetime.now()}
        feg.insert_one(dialog)
        return redirect(url_for('index'))

    all_feg = list(feg.find())
    return render_template('index.html', feg=all_feg)

@app.route('/<id>/sentences/', methods=('GET', 'POST'))
def sentences(id):
    if request.method=='POST':
        sentences = request.form['sentences']
        res = feg.aggregate([{'$sample': {'size': 1 }}])
        randomName =list(res)
        sentence={'ReceiverName': randomName[0]['Name'], 'Sentence': sentences, 'Seen': False, 'TimeStamp': '', 'Sent': False, 'CreatedBy': '', 'CreatedDate': datetime.now(), 'ModifiedBy':'', 'ModifiedDate': datetime.now(), 'DialogId':ObjectId(id)}
        todos.insert_one(sentence)

        return redirect(url_for('index'))

    all_feg = list(feg.find())
    return render_template('index.html', feg=all_feg)

@app.route('/replay_dialog', methods=('GET', 'POST'))
def replay_dialog():
    if request.method=='POST':
        replay_dialog = request.form['replay_dialog']
        for i in sentences:
            res = feg.aggregate([{'$sample': {'size': 1 }}])
            randomName =list(res)
            sentence={'ReceiverName': randomName[0]['Name'], 'Sentence': i['Sentence'], 'Seen': False, 'TimeStamp': '', 'Sent': False, 'CreatedBy': '', 'CreatedDate': datetime.now(), 'ModifiedBy':'', 'ModifiedDate': datetime.now(), 'DialogId':ObjectId(replay_dialog)}
            todos.insert_one(sentence)
        return redirect(url_for('index'))

    all_feg = list(feg.find())
    return render_template('index.html', feg=all_feg)

@app.post('/<id>/delete/')
def delete(id):
    feg.delete_one({"_id": ObjectId(id)})
    return redirect(url_for('index'))

@app.post('/<id>/get_row/')
def get_row(id):
    todos.update_one({"_id": ObjectId(id)},{"$set":{"Sent":True}})
    return redirect(url_for('index'))

@app.post('/send_all_dialog')
def send_all_dialog():
    todos.update_many({"Sent": False},{"$set":{"Sent":True}})
    return redirect(url_for('index'))

@app.post('/<id>/disable/')
def disable(id):
    user.update_one({"_id": ObjectId(id)},{"$set":{"Online":False}})
    return redirect(url_for('index'))

