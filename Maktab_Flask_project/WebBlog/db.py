from mongoengine import *

connect(host="mongodb://127.0.0.1:27017/my_db")


class Category(DynamicDocument):
    name = StringField(max_length=50)
    parent_cat = ReferenceField('self', required=False)


class Tag(DynamicDocument):
    name = StringField(max_length=50)
