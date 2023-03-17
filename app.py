from flask import Flask
from pymongo import MongoClient
import config as cfg

from index_blueprint import index_blueprint
from dialog_blueprint import dialog_blueprint
from new_user_blueprint import new_user_blueprint
from sentences_blueprint import sentences_blueprint
from replay_dialog_blueprint import replay_dialog_blueprint
from show_dialog_blueprint import show_dialog_blueprint
from send_blueprint import send_blueprint
from skip_blueprint import skip_blueprint
from send_dialog_blueprint import send_dialog_blueprint
from disable_blueprint import disable_blueprint

app = Flask(__name__)
app.register_blueprint(index_blueprint)
app.register_blueprint(dialog_blueprint)
app.register_blueprint(new_user_blueprint)
app.register_blueprint(sentences_blueprint)
app.register_blueprint(replay_dialog_blueprint)
app.register_blueprint(show_dialog_blueprint)
app.register_blueprint(send_blueprint)
app.register_blueprint(skip_blueprint)
app.register_blueprint(send_dialog_blueprint)
app.register_blueprint(disable_blueprint)

client = MongoClient(cfg.dbUrl)

db = client.FunEnglistGamePrj_Web
Dialog = db.Dialog
EnglishSentence = db.EnglishSentence
Users = db.Users
DialogContentNotification = db.DialogContentNotification

dialog_find = list(Dialog.find().sort("ModifiedDate", -1).limit(1))
show_Dialog = dialog_find[0]['_id']

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9999)