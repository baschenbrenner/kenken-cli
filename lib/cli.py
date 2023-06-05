#!/usr/bin/env python3

from models import User, Game, Note
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from helpers import produce_board
import json



class CLI:

    def __init__(self):
        self.users = [u for u in session.query(User)]
        self.games = [g for g in session.query(Game)]
        self.notes = [n for n in session.query(Note)]
        self.user_info = self.get_name()
        self.main_menu()
        # self.start()

    # Was going to make a dict mapped to choices, but seems like we would still need an if
    # statement so maybe an unneeded abstraction
    # def options_dict(self):
    #     return {
    #         'pa': self.print_indexed_items(self.authors, 'name'),
    #     }

    def get_name(self):
        print("Welcome to our Kenken App")
        print("Please give us your name!")
        u_name = input("What is your user name?")
        new_user = None
        print("Thanks!")
        usernames = [u.name for u in session.query(User)]
        if u_name in usernames:
            print(f"Is that you, {u_name}?!")
            special_word = input("What is your special word? \n Case doesn't matter \n Type here: ")
            user = session.query(User).filter_by(name=u_name).first()
            if special_word.lower() == user.special.lower():
                print(f"Welcome Back {u_name}!")
                return user
            else:
                print("You forgot your special word!")
                #add looping, second try
                quit()
        else:
            print("Welcome to our Kenken App!")
            special_word = input("What is your special word? \nThis will be used to remember you in the future and prevent posers from playing your games.\n It should be longer than 3 letters.\n Type here: ")
            confirm = input("Type again for confirmation: ")
            if special_word==confirm and len(confirm) > 3:
                new_user = User(name=u_name,special=confirm)
                session.add(new_user)
                session.commit()
                #add rescue for value error instead of error handling 
            else:
                print("Something went wrong. Try again.")
                quit()

        return new_user
        #error handling for weird input?
    def main_menu(self):
        choice = ''
        while (not CLI.valid_choice(['new', 'prev', 'exit'], choice)):
            print('\033[1;32;40m|To play a new game enter "new"|\n')
            print('\033[1;32;40m|To see previous games enter "prev"|\n')
            print('\033[1;32;40m|To exit type "exit" "prev"|\033[0;37;40m \n')
            choice = input("Type your choice here: ")
            if choice == "exit":
                print(f"Goodbye {self.user_info.name}!")
                quit()
            if choice == "new":
                print("let's play new game!")
                new_game = Game(user_id=self.user_info.id)
                session.add(new_game)
                session.commit()
                produce_board(json.loads(new_game.groupings), json.loads(new_game.pairs))
        print("\033[0;37;40m ***************************")
        print("Where would you like to play?")
        quit()
        

   


    @ classmethod
    def valid_choice(self, options, input):
        return input in options



if __name__ == "__main__":
    engine = create_engine('sqlite:///models.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    CLI()

# For addign a review
