from flask import Flask, render_template, request, url_for, redirect
from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import datetime


app = Flask(__name__)

client = MongoClient('mongodb://localhost:27017/')
# c = MongoClient(103.116.106.153:2718)
# app.config["MONGO_URI"] = "mongodb://localhost:27017/feg"
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
        feg.insert_one({'sentences': sentences, 'dialog': new_dialog})
        return redirect(url_for('index'))

    all_feg = list(feg.find())
    all_todos = list(todos.find())
    all_Dialog = list(Dialog.find())
    all_Dialog_reverse = reversed(all_Dialog)
    all_Users = list(Users.find())
    all_EnglishSentence = list(EnglishSentence.find())
    all_DialogContentNotification = list(DialogContentNotification.find())
    
    return render_template('index.html', feg=all_feg, todos=all_todos, 
    Dialog=all_Dialog, Users=all_Users, EnglishSentence=all_EnglishSentence, DialogContentNotification=all_DialogContentNotification,
    Dialog_reverse=all_Dialog_reverse)

@app.route('/new_dialog', methods=('GET', 'POST'))
def new_dialog():
    if request.method=='POST':
        new_dialog = request.form['new_dialog']
        dialog ={'Name': new_dialog,'CreatedBy': '', 'Date': datetime.now(), 'ModifiedBy': '', 'ModifiedDate': datetime.now()}
        feg.insert_one(dialog)
        return redirect(url_for('index'))

    all_feg = list(feg.find())
    return render_template('index.html', feg=all_feg)

# @app.route('/dialog', methods=('GET', 'POST'))
# def dialog():
    # if request.method=='POST':
    #     dialog = request.form['dialog']
    #     feg.insert_one({'dialog': new_dialog})
    #     return redirect(url_for('index'))

    # all_feg = list(feg.find())
    # return render_template('index.html', feg=all_feg)

@app.route('/sentences', methods=('GET', 'POST'))
def sentences():
    if request.method=='POST':
        sentences = request.form['sentences']
        dialog=feg.find().sort("Date", -1)
        sentence={'ReceiverName': '', 'Sentence': sentences, 'Seen': '', 'TimeStamp': '', 'DialogId':dialog[0]._id}
        feg.insert_one(sentence)

        return redirect(url_for('index'))

    all_feg = list(feg.find())
    return render_template('index.html', feg=all_feg)

@app.post('/<id>/delete/')
def delete(id):
    feg.delete_one({"_id": ObjectId(id)})
    return redirect(url_for('index'))

@app.post('/<id>/get_row/')
def get_row(id):
    feg.delete_one({"_id": ObjectId(id)})
    return redirect(url_for('index'))

@app.post('/<id>/find/')
def find(id):
    feg.delete_one({"_id": ObjectId(id)})
    return redirect(url_for('index'))

