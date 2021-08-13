from mongoengine import *

connect(host="mongodb://127.0.0.1:27017/my_db")


class User(DynamicDocument):
    username = StringField(max_length=50)
    email = StringField(required=True)
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)
    phone_number = StringField(max_length=50)
    password = StringField(max_length=50)



