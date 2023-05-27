from sqlalchemy import create_engine, func
from sqlalchemy import ForeignKey, Table, Column, Integer, String, DateTime, MetaData
from sqlalchemy.orm import relationship, backref, validates
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import random


convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)

engine = create_engine('sqlite:///models.db')
Session = sessionmaker(bind=engine)
session = Session()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    created_at = Column(DateTime(), server_default=func.now())

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
    created_at = Column(DateTime(), server_default=func.now())


    @classmethod
    def create_and_add_to_cli(self, name, cli):
        game = Game(result="in progress")
        session.add(game)
        session.commit()
        cli.games.append(game)
    
    def create_board(self):
        def find_missing(arr):
            start = [1,2,3,4]
            for x in arr:
                start.remove(x)
            return start[0]

        board = []
        row1 = []
        row1.append(random.randrange(1,5))
        while len(row1)<4:
            curr_length = len(row1)
            if (curr_length == 3):
                    num = find_missing(row1)
                    row1.append(num)
            new_num = random.randrange(1,5)
            while new_num not in row1:
                row1.append(new_num)
                new_num = random.randrange(1,5)

        board.append(row1)
        
        row2=[]
        finished = False
        while finished == False:

            while len(row2)<4:
                new_num = random.randrange(1,5)
                curr_length = len(row2)
                while curr_length != 4 and row1[curr_length] != new_num:
                    if (new_num not in row2):
                        row2.append(new_num) 
                        curr_length+=1
                    elif (curr_length == 3):
                        num = find_missing(row2)
                        row2.append(num)
                        curr_length+=1
                    new_num = random.randrange(1,5)

            if row2[3] == row1[3]:
                row2=[]
            else:
                finished=True
                
        board.append(row2)
        

        finished = False
        row3=[]
        while finished == False:
            
            while len(row3)<4:
                new_num = random.randrange(1,5)
                curr_length = len(row3)
                while (curr_length != 4) and (row1[curr_length] != new_num) and (row2[curr_length] != new_num):
                    if curr_length == 1:
                        check_array = [*set([row1[0],row1[1],row2[0],row2[1],row3[0]])]
                        if len(check_array) == 3:
                            row3.append(find_missing(check_array))
                            curr_length+=1
                        else:
                            if new_num not in row3:
                                row3.append(new_num)
                                curr_length+=1

                    elif new_num not in row3:
                        row3.append(new_num)
                        curr_length+=1
                    elif (curr_length == 3):
                        num = find_missing(row3)
                        row3.append(num)
                        curr_length+=1
                    new_num = random.randrange(1,5)

                    if curr_length==2 and sorted([row3[0], row3[1], row1[2], row2[2]]) == [1,2,3,4]:
                        row3 = []
                        curr_length=0

            
            if row3[3]==row1[3] or row3[3]==row2[3]:
                    row3 = []
            else:
                finished = True

            



        board.append(row3)
        # print("------------------")
        # for row in board:
        #     print(row)
        row4 = [find_missing([row1[0],row2[0],row3[0]]),find_missing([row1[1],row2[1],row3[1]]), find_missing([row1[2],row2[2],row3[2]]), find_missing([row1[3],row2[3],row3[3]])]
        board.append(row4)
        # print("here's your board!")
        # print("------------------")
        # for row in board:
        #     print(row)
        

        board_rep = {}
        counter = 1 
        for x in range(4):
            for y in range(4):
                board_rep[counter]=board[x][y]
                counter+=1
        self.board = board
        self.board_rep = board_rep
        return (board, board_rep)

    notes = relationship('Note', backref=backref('game'))

    def __repr__(self):
        return f'<#Game(id={self.id} result={self.result} user={self.user})>'


class Note(Base):
    __tablename__ = 'notes'

    id = Column(Integer(), primary_key=True)
    content = Column(String())
    rating = Column(Integer())
    game_id = Column(Integer, ForeignKey('games.id'))
    created_at = Column(DateTime(), server_default=func.now())

    

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
