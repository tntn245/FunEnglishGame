from flask import render_template, request, url_for, redirect, Blueprint
from bson.objectid import ObjectId
from datetime import datetime
from sentence import SentenceDTO
import db as app

sentences_blueprint = Blueprint('sentences_blueprint', __name__)

@sentences_blueprint.route('/sentences/<id>/', methods=('GET', 'POST'))
def sentences(id):
    if request.method=='POST':
        sentences = request.form['sentences']
        list_sentences = sentences.splitlines()
        for i in list_sentences:
            randomName = list(app.Users.aggregate([{ '$match': {'Online': True}},{'$sample': {'size': 1 }}]))
            sentence = SentenceDTO(randomName[0]['PCName'],i,False,'',False,'',datetime.now(),'',datetime.now(),ObjectId(id))
            app.EnglishSentence.insert_one(sentence.__dict__)
        return redirect(url_for('index_blueprint.index'))

    all_EnglishSentence = list(app.EnglishSentence.find())
    return render_template('index.html', EnglishSentence=all_EnglishSentence)