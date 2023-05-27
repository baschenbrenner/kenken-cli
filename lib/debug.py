from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User, Game, Note

import ipdb;


if __name__ == '__main__':
    
    engine = create_engine('sqlite:///models.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    ipdb.set_trace()