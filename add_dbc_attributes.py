import os
import cantools
from attribute_definitions import attribute_def_list

def add_attributes(file):
    db = cantools.database.load_file(file)
    for message in db.messages:
        for attribute in attribute_def_list:
            if attribute.name not in message.dbc.attribute_definitions:
                message.dbc.attribute_definitions[attribute.name] = attribute
        break
    cantools.database.dump_file(db, file)

def main():
    files = filter(os.path.isfile, os.listdir(os.curdir))
    for file in files:
        if os.path.splitext(file)[1] == ".dbc":
            if os.access(file, os.W_OK) and os.access(file, os.R_OK):
                add_attributes(file)
    return

if __name__ == "__main__":
    main()

