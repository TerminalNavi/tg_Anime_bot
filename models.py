'''Импорт модулей для модуля ДБ'''
from peewee import SqliteDatabase, Model, TextField, ForeignKeyField, IntegerField

db = SqliteDatabase('sqlite.db')

class DB(Model):
    '''Заготовка под БД'''
    class Meta:
        '''Я без понятия, что ЭТО'''
        database = db

class User(DB):
    '''Запись в базе данных.
    Имеет два поля - id чата и последняя отправленная ссылка'''
    user_id = IntegerField()

class Anime(DB):
    url = TextField()

class UserAnime(DB):
    user = ForeignKeyField(User, backref='animes')
    anime = ForeignKeyField(Anime)


db.connect()
db.create_tables([User, Anime, UserAnime], safe=True)
db.close()
