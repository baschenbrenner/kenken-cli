#!/usr/bin/env python3

from models import User, Game, Note
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from helpers import produce_board, check_num, board_in_play, games_menu, process_solution, check_input_num
import json



class CLI:

    def __init__(self):
        self.users = [u for u in session.query(User)]
        self.games = [g for g in session.query(Game)]
        self.notes = [n for n in session.query(Note)]
        self.user_info = self.get_name()
        self.main_menu(self.user_info)
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
        u_name = input("What is your user name? ")
        new_user = None
        print("Thanks!")
        users = [u for u in session.query(User).all()]
        usernames = [u.name.lower() for u in users]
        if u_name.lower() in usernames:
            print(f"Is that you, {u_name}?!")
            special_word = input("What is your special word? \n Case doesn't matter \n Type here: ")
            ind = usernames.index(u_name.lower())
            potential_user = users[ind]
            if special_word.lower() == potential_user.special.lower():
                print(f"Welcome Back {u_name}!")
                return potential_user
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


    def main_menu(self, user):
        choice = ''
        while (not CLI.valid_choice(['new', 'prev', 'exit', 'users'], choice)):
            print('\033[1;32;40m|To play a new game enter "new"|\n')
            print('\033[1;32;40m|To see previous games enter "prev"|\n')
            print('\033[1;32;40m|To exit type "exit"|\033[0;37;40m \n')
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
                self.play_game(new_game.id)
            if choice == "prev":
                games = session.query(Game).filter_by(user_id=user.id).all()
                print(" ID |   RESULT   | TIME (s) ")
                game_ids = []
                for g in games:
                    result_str = " " + g.result
                    length_of_str = len(result_str)
                    final_str = result_str + " "*(12-length_of_str)
                    id = str(g.id)+" "
                    length_of_id = len(id)
                    final_string = " "*(4-len(id))+id+"|"
                    game_ids.append(g.id)
                    if g.duration() == 0 or g.duration() == 1:
                        print(final_string+final_str+"|       N/A")
                    else:
                        dur = str(g.duration())+" "
                        length_of_dur = len(dur)
                        last_string = " "*(10-length_of_dur) + dur
                        print(final_string+final_str+"|"+last_string)
                choice = games_menu()
                if choice=="exit":
                    quit()
                elif choice=="users":
                    users = session.query(User).all()
                    print("ID | NAME ")
                    print("-----------")
                    for u in users: 
                        print(str(u.id) +". " + u.name)
                    choice = input("choose an id to see games results, or any other key to go back up to the main menu")
                    if check_num(choice):
                        #error handling for number entered not in list
                        games = session.query(Game).filter_by(user_id=check_num(choice)).all()
                        for g in games:
                            result_str = " " + g.result
                            length_of_str = len(result_str)
                            final_str = result_str + " "*(12-length_of_str)
                            id = str(g.id)+" "
                            length_of_id = len(id)
                            final_string = " "*(4-len(id))+id+"|"
                            if g.duration() == 0 or g.duration() == 1:
                                print(final_string+final_str+"|       N/A")
                            else:
                                dur = str(g.duration())+" "
                                length_of_dur = len(dur)
                                last_string = " "*(10-length_of_dur) + dur
                                print(final_string+final_str+"|"+last_string)
                    else:
                        choice=""
                elif int(choice) in game_ids:
                    selected_game = session.query(Game).filter_by(id=int(choice)).first()
                    board_in_play(json.loads(selected_game.groupings), json.loads(selected_game.pairs), process_solution(json.loads(selected_game.solution_dict)))
                    print("NOTES:\n")
                    notes = selected_game.notes
                    if notes:
                        for n in notes:
                            print(n.content + "\n")
                    else:
                        print("No notes yet!\n")
                        if input("Would you like to make an new note (y/n): ") == "y":
                            #error handling - or different flow - I read this too fast and just entered a note and then my note got lost
                            comment = input("Type your note here: ")
                            new_note = Note(content=comment, game_id=selected_game.id)
                            session.add(new_note)
                            session.commit()
                            choice=''

        
        quit()

    def play_game(self, game_id):
        #load game locally
        found_game = session.query(Game).filter_by(id=game_id).first()

        solution = {}
        counter = 1 
        while (counter < 17):
            solution[counter]=" "
            counter+=1

        print("\033[0;37;40m ***************************")
        in_progress = True
        found_game.result = "in progress"
        session.add(found_game)
        session.commit()
        gr = json.loads(found_game.groupings)
        pa = json.loads(found_game.pairs)

        while in_progress:
            choice=None
            while (not choice):
                choice = input("What cell number would you like to play in (use the red grid for reference): ")
                if choice == 'q':
                    quit()
                choice = check_num(choice)
               
            if solution.get(choice) == " ":  
                print("What number will you place here?")
                num = None
                while (not num):
                    num = input("Type your choice here: ")
                    num = check_input_num(num)
                
                # create logic to evaluate if the move is correct - if not give feedback to choose a different number 
                
                solution[choice]=int(num)
                board_in_play(gr, pa, solution)
                if " " not in solution.values():
                    from_db = json.loads(found_game.solution_dict)
                    result = "won"
                    for k in solution.keys():
                        if solution[k] != from_db[str(k)]:
                            result = "lost"
                    if result == "won":
                        found_game.result = "won"
                        print("\033[0;37;41mYOU WON!\033[1;37;40m")
                        if input("Would you like to make an new note (y/n): ") == "y":
                            comment = input("Type your note here: ")
                            new_note = Note(content=comment, game_id=found_game.id)
                            session.add(new_note)
                            session.commit()
                            choice=''
                        
                    else:
                        found_game.result = "lost"
                    session.add(found_game)
                    session.commit()
                    self.main_menu(self.user_info)
            elif solution.get(choice) == None:
                print("That space does not exist!")
                choice=None  
            else:
                print('\033[1;32;40m|To delete entry enter "del"|\n')
                print('\033[1;32;40m|To change entry enter "ch"|\n')
                print('\033[1;32;40m|To go back to cell selection type "sel"|\033[0;37;40m \n')
                play = input(f"What would you like to do in cell {choice}: ")
                if play == "del":
                    solution[choice]=' '
                    board_in_play(gr, pa, solution)
                if play == "ch":
                    print("What number will you change this cell to?")
                    num = input("Type your choice here: ")
                    solution[choice]=int(num)
                    board_in_play(gr, pa, solution)
                    if " " not in solution.values():
                        if solution == json.loads(found_game.solution_dict):
                            found_game.result = "won"
                        else:
                            #create a method to evaluate their board to determine if it is a logically sound alternative solution
                            found_game.result = "lost"
                        session.add(found_game)
                        session.commit()
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
