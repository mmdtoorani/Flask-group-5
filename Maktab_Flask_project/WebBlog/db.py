from mongoengine import *

connect(host="mongodb://127.0.0.1:27017/my_db")


class Category(DynamicDocument):
    name = StringField(max_length=50)
    parent_cat = ReferenceField('self', required=False)


class Tag(DynamicDocument):
    name = StringField(max_length=50)


class User(DynamicDocument):
    username = StringField(max_length=50)
    email = StringField(max_length=50, required=False)
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)
    phone_number = StringField(max_length=50)
    password = StringField(max_length=50)



class Post(DynamicDocument):
    title = StringField(max_length=50)
    body = StringField(max_length=250)
    status = IntField()
    photo = FileField()
    likes = ListField()
    dislikes = ListField()
    user = ReferenceField('User', reverse_delete_rule=CASCADE)
    cat = ReferenceField('Category', reverse_delete_rule=CASCADE)
    tags = ListField()
