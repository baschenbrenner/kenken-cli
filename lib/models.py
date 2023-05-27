from sqlalchemy import create_engine, func
from sqlalchemy import ForeignKey, Table, Column, Integer, String, DateTime, MetaData
from sqlalchemy.orm import relationship, backref, validates
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)

engine = create_engine('sqlite:///lib/models.db')
Session = sessionmaker(bind=engine)
session = Session()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer(), primary_key=True)
    name = Column(String())

    @validates('name')
    def check_name(self, key, string):
        print(key)
        print(string)
        return string
    

    games = relationship('Game', backref=backref('user'))

    def __repr__(self):
        return f'<#User(id={self.id} name={self.name} games={self.games})>,'



class Game(Base):
    __tablename__ = 'games'

    id = Column(Integer(), primary_key=True)
    result = Column(String())
    user_id = Column(Integer(), ForeignKey('users.id'))


    @classmethod
    def create_and_add_to_cli(self, name, cli):
        game = Game(result="in progress")
        session.add(game)
        session.commit()
        cli.games.append(game)

    notes = relationship('Note', backref=backref('game'))

    def __repr__(self):
        return f'<#Game(id={self.id} result={self.result} user={self.user})>'


class Note(Base):
    __tablename__ = 'notes'

    id = Column(Integer(), primary_key=True)
    content = Column(String())
    rating = Column(Integer())
    game_id = Column(Integer, ForeignKey('games.id'))

    

    def __repr__(self):
        return f'<#Note(id={self.id} content={self.content} game_id={self.game_id} )>,'


# class Review(Base):
#     # id:Integer,
#     # Comment: String
#     # Name: string
#     # Book_id:(Foreign Key)

#     __tablename__ = 'reviews'

#     id = Column(Integer(), primary_key=True)
#     comment = Column(String())
#     name = Column(String())
#     book_id = Column(Integer, ForeignKey('books.id'))

#     def __repr__(self):
#      return f'<#Review(id={self.id} name={self.name} comment={self.comment})>,'
