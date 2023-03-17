from pymongo import MongoClient
import config as cfg

client = MongoClient(cfg.dbUrl)
db = client.FunEnglistGamePrj_Web
Dialog = db.Dialog
EnglishSentence = db.EnglishSentence
Users = db.Users
DialogContentNotification = db.DialogContentNotification
dialog_find = list(Dialog.find().sort("ModifiedDate", -1).limit(1))
show_Dialog = dialog_find[0]['_id']