'''Импорт модулей для модуля ДБ'''
from peewee import SqliteDatabase, Model, TextField

db = SqliteDatabase('sqlite.db')

class DB(Model):
    '''Заготовка под БД'''
    class Meta:
        '''Я без понятия, что ЭТО'''
        database = db

class User(DB):
    '''Запись в базе данных.
    Имеет два поля - id чата и последняя отправленная ссылка'''
    user_id = TextField()
    anime_url = TextField(default='None')


db.connect()
db.create_tables([User], safe=True)
db.close()
