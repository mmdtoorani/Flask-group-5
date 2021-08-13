from mongoengine import *

connect(host="mongodb://127.0.0.1:27017/my_db")

class User(DynamicDocument):
    username = StringField(max_length=50)