import os
from model.datadase import DATABASE_NAME, Session
import creat_database39 as db_creator

if __name__ == "__main__":
    db_is_created = os.path.exists(DATABASE_NAME)
    if not db_is_created:
        db_creator.create_database()

    session = Session()
