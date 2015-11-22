import datetime

from peewee import *

DATABASE = SqliteDatabase('blog.db')

class BaseModel(Model):
    class Meta:
        database = DATABASE

class Post(BaseModel):
    post_name = CharField(max_length=255)
    post_content = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)
    reading_time = IntegerField(default=5)
    class Meta:
        order_by = ('-created_at',)



def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Post], safe=True)
    DATABASE.close()

initialize()
