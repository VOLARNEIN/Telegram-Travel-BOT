import sqlalchemy

from .db_session import SqlAlchemyBase


class Translations(SqlAlchemyBase):
    __tablename__ = 'translations'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    user_id = sqlalchemy.Column(sqlalchemy.Integer)
    first_language = sqlalchemy.Column(sqlalchemy.String)
    second_language = sqlalchemy.Column(sqlalchemy.String)

    def __repr__(self):
        return f'{self.id} {self.user_id} {self.first_language} {self.second_language}'
