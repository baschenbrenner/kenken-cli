from sqlalchemy import create_engine, func
from sqlalchemy import ForeignKey, Table, Column, Integer, String, DateTime, MetaData
from sqlalchemy.orm import relationship, backref, validates
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from helpers import random_50, random_33, analyze_left
import random
import json


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
    special = Column(String())
    created_at = Column(DateTime(), server_default=func.now())

    def __init__(self, name="", special=""):
        self.name = name
        self.special=special.lower()



    @validates('name', 'special')
    def check_name(self, key, string):
        users = session.query(User).all()
        if key == 'name':
            if string in [u.name for u in users]:
                raise ValueError("That user name is already taken")
            if string == '':
                raise ValueError("You must provide a user name")
            return string
        elif key == "special":
            if string == '':
                raise ValueError("You must provide a special word")
            if len(string) < 4:
                raise ValueError("Your special word must be longer than 3 letters")
            return string
        

    games = relationship('Game', backref=backref('user'))

    def __repr__(self):
        return f'#<User(id={self.id} name={self.name} games={[g.id for g in self.games]})>,'



class Game(Base):
    __tablename__ = 'games'

    id = Column(Integer(), primary_key=True)
    result = Column(String())
    user_id = Column(Integer(), ForeignKey('users.id'))
    groupings = Column(String())
    created_at = Column(DateTime(), server_default=func.now())
    updated_at = Column(DateTime(), onupdate=func.now())
    board = Column(String())
    pairs = Column(String())
    solution_dict=Column(String())

    def __init__(self, user_id):
        board_tuple = self.create_board()
        self.board = json.dumps(board_tuple[0])
        self.solution_dict=json.dumps(board_tuple[1])
        groups = self.produce_groupings()
        self.groupings = json.dumps(groups)
        self.user_id = user_id
        self.result="created"
        self.pairs = json.dumps(self.random_operations(board_tuple, groups))

    @classmethod
    #create_board produces a tuple with board (array of arrays) and board dict

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

    #produce groupings produces an array of arrays

    def produce_groupings(self):
        group1 = [1]

        #groupings - start with 1, try 2, if not 2 then add 5, then try 9  if 9, then done, if not 9 try 6. else try 5, 

        if random_50():
            group1.append(2)
            if random_33():
                group1.append(5)
            elif random_33():
                group1.append(6)
            else:
                if random_33():
                    group1.append(3)
        else:
            group1.append(5)
            if random_33():
                group1.append(9)



        group2 = []
        if 2 in group1:
            if 3 in group1:
                group2.append(4)
                group2.append(8)
            else:
                group2.append(3)
                if random_50():
                    group2.append(4)
                else:
                    group2.append(7)
        else:
            group2.append(2)
            if random_50():
                group2.append(3)
            else:
                group2.append(6)
        result = [group1,group2]
        flattened = [num for sublist in result for num in sublist]
        group3=[]
        if 3 not in flattened:
            group3.append(3)
            group3.append(4)
            if random_50():
                if 7 not in flattened:
                    group3.append(7)
        elif 4 not in flattened:
            group3.append(4)
            group3.append(8)
        elif 5 not in flattened:
            group3.append(5)
            if 6 not in flattened:
                group3.append(6)
            else:
                group3.append(9)
        elif 6 not in flattened:
            group3.append(6)
            group3.append(7)



        result = [group1,group2,group3]
        flattened = [num for sublist in result for num in sublist]

        group4=[]
        if 5 not in flattened:
            group4.append(5)
            if 6 not in flattened:
                group4.append(6)
            else:
                group4.append(9)
        elif 6 not in flattened:
            group4.append(6)
            if 7 not in flattened:
                group4.append(7)
            else:
                group4.append(10)
        elif 7 not in flattened:
            group4.append(7)
            if 8 not in flattened:
                group4.append(8)
            else:
                group4.append(11)
        elif 8 not in flattened:
            group4.append(8)
            group4.append(12)
            

        result = [group1,group2,group3, group4]
        flattened = [num for sublist in result for num in sublist]
        # print(sorted(flattened))

        group5=[]
        if 9 not in flattened:
            group5.append(9)
            if 10 not in flattened:
                group5.append(10)
                group5.append(14)
            else:
                group5.append(13)
        elif 10 not in flattened:
            group5.append(10)
            if 11 not in flattened:
                group5.append(11)
            else:
                group5.append(14)


        result = [group1,group2,group3, group4, group5]
        flattened = [num for sublist in result for num in sublist]

        group6=[]
        if 11 not in flattened:
            group6.append(11)
            if 12 not in flattened:
                group6.append(12)
            else:
                group6.append(15)
        elif 12 not in flattened:
            group6.append(12)
            group6.append(16)

        result = [group1,group2,group3, group4, group5, group6]
        flattened = [num for sublist in result for num in sublist]

        left =[]
        for x in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]:
                
            if x not in flattened:
                left.append(x)
        
        final_groupings = analyze_left(left)
        for l in final_groupings:
            result.append(l)

        # flattened = [num for sublist in result for num in sublist]
        # if len(flattened)==len(set(flattened)):
        #     print("TRUE!")
        # else:
        #     print("Something went wrong")
        if [] in result:
            result.remove([])
        return result
    
    #random operations produces an array of tuples with operation and result

    def random_operations(self, tup, groups):
        result=[]
        options =["+","-","x","/"]
        counter = 0
        while counter < len(groups):
        #   print(groups[counter])
            if len(groups[counter]) == 1:
                result.append((" ", tup[1][groups[counter][0]]))
            elif len(groups[counter]) == 2:
                op = random.choice(options)
                if op == "+":
                    end = tup[1][groups[counter][0]] + tup[1][groups[counter][1]]
                    result.append(("+", end))
                elif op == "-":
                    if tup[1][groups[counter][0]] - tup[1][groups[counter][1]] > 0:
                            end = tup[1][groups[counter][0]] - tup[1][groups[counter][1]]
                            result.append(("-", end))
                    else:
                        end = tup[1][groups[counter][1]] - tup[1][groups[counter][0]]
                        result.append(("-", end))
                elif op == "x":
                    end = tup[1][groups[counter][0]] * tup[1][groups[counter][1]]
                    result.append(("x", end))
                elif op == "/":
                    if tup[1][groups[counter][0]]/tup[1][groups[counter][1]] == 2:
                        end = 2
                        result.append(("/", end))
                    elif tup[1][groups[counter][1]]/tup[1][groups[counter][0]] == 2:
                        end = 2
                        result.append(("/", end))
                    elif tup[1][groups[counter][1]]/tup[1][groups[counter][0]] == 3:
                        end = 3
                        result.append(("/", end))
                    elif tup[1][groups[counter][0]]/tup[1][groups[counter][1]] == 3:
                        end = 3
                        result.append(("/", end))
                    elif tup[1][groups[counter][1]]/tup[1][groups[counter][0]] == 4:
                        end = 4
                        result.append(("/", end))
                    elif tup[1][groups[counter][0]]/tup[1][groups[counter][1]] == 4:
                        end = 4
                        result.append(("/", end))
                    else:
                        end = tup[1][groups[counter][0]] * tup[1][groups[counter][1]]
                        result.append(("x", end))
            elif len(groups[counter]) == 3:
                if random_50():
                    end = tup[1][groups[counter][0]] * tup[1][groups[counter][1]]*tup[1][groups[counter][2]]
                    result.append(("x", end))
                else:
                    end = tup[1][groups[counter][0]] + tup[1][groups[counter][1]]+tup[1][groups[counter][2]]
                    result.append(("+", end))

            counter += 1

        return result
    

    def duration(self):
        return (self.updated_at-self.created_at).seconds
    
    notes = relationship('Note', backref=backref('game'))

    def __repr__(self):
        return f'#<Game(id={self.id} result={self.result} user={self.user})>'


class Note(Base):
    __tablename__ = 'notes'

    id = Column(Integer(), primary_key=True)
    content = Column(String())
    game_id = Column(Integer, ForeignKey('games.id'))
    created_at = Column(DateTime(), server_default=func.now())

    

    def __repr__(self):
        return f'#<Note(id={self.id} content={self.content} game_id={self.game_id} )>,'


