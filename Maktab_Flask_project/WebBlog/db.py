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


for cat in Category.objects:
    print(cat.name)
    print(cat.id)
    print('----------')

for post in Post.objects:
    print(post.title)
    if post.cat:
     print(post.cat[0])
    print('========')
# Tag.drop_collection()

def category(category_id):
    list_of_cats = [category_id]
    posts=[]
    for cat in Category.objects:
        if str(cat.parent_cat) in list_of_cats:
            list_of_cats.append(str(cat.id))

    for post in Post.objects:
        print('2')
        print(str(post.cat[0]))
        print(list_of_cats)
        if str(post.cat[0]) in list_of_cats:
            print('3')
            posts.append(post)

    return posts
print(category('61241a4138bf5af4f076d646'))
# Post.drop_collection()
# Category.drop_collection()
# tag1 = Tag(name='mohseni')
# tag1.save()
# post1 = Post(title='this post', tags=[str(tag1.id)])
# post1.save()
# print(Post.objects(tags__in=['61239632178a94f45f36625a'])[0].title)
# posts = Post.objects(tags__in=['61240a7390130f3c3bbbafb9'])
# print(posts)
# cat1 = Category(name='movies')
# cat2 = Category(name='horror', parent_cat=cat1.id)
# cat1.save()
# cat2.save()
#
# post = Post(title='test for category', cat=[str(cat2.id)])
# post.save()