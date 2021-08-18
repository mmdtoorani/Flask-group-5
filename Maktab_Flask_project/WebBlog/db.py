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
    password = StringField(max_length=250)


class Post(DynamicDocument):
    title = StringField(max_length=50)
    body = StringField(max_length=250)
    status = IntField()
    photo = StringField(max_length=250)
    likes = ListField()
    dislikes = ListField()
    user = ReferenceField('User', reverse_delete_rule=CASCADE)
    cat = ReferenceField('Category', reverse_delete_rule=CASCADE)
    tags = ListField()



# how to add a picture in mongoengine
# class Animal(Document):
#     genus = StringField()
#     family = StringField()
#     photo = FileField()
#
# marmot = Animal(genus='Marmota', family='Sciuridae'
# with open('marmot.jpg', 'rb') as fd:
#     marmot.photo.put(fd, content_type = 'image/jpeg')
# marmot.save()



# some examples of db
# tag1 = Tag(name='johnny depp')
# tag1.save()
# tag2 = Tag(name='pirate')
# tag2.save()
#
# cat1 = Category(name='film')
# cat2 = Category(name='comedy', parent_cat=cat1)
# cat1.save()
# cat2.save()
#
# user1 = User(username='mohammad', email='mohammad@gmail.com', first_name='mohammad', lastname='mohammad',
#              phone_number='09371418637', password='mohammad')
# user1.save()
#
# post1 = Post(title='pirates', body='loskvmkffvakflv', status=3, user=user1, cat=cat2, likes=[user1])
# post1.save()
#
# print(cat2.id)
# print(post1.tags)
# print(post1.likes)
