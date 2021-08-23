from mongoengine import *

connect(host="mongodb://127.0.0.1:27017/my_db")


class Category(DynamicDocument):
    name = StringField(max_length=50)
    parent_cat = ReferenceField('self', required=False)


class Tag(DynamicDocument):
    name = StringField(max_length=50)
    posts = ListField()


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
    cat = ListField()
    tags = ListField()


# Post.drop_collection()
# Tag.drop_collection()
#
# tag1 = Tag(name='ali')
# tag2 = Tag(name='reza')
# tag1.save()
# tag2.save()
# post1=Post(title='ali', tags=[str(tag1.id), str(tag2.id)])
# post1.save()

for tag in Tag.objects:
    print(tag.name)
    print(tag.id)
    print('----------')

for post in Post.objects:
    print(post.title)
    print(post.tags)
    print('========')
# Tag.drop_collection()
# Post.drop_collection()
# tag1 = Tag(name='mohseni')
# tag1.save()
# post1 = Post(title='this post', tags=[str(tag1.id)])
# post1.save()
# print(Post.objects(tags__in=['61239632178a94f45f36625a'])[0].title)
posts = Post.objects(tags__in=['61240a7390130f3c3bbbafb9'])
print(posts)