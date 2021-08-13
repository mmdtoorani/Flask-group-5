from .db import *


class User(Document):
    username = StringField(max_length=50)
    email = StringField(required=True)
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)
    phone_number = StringField(max_length=50)
