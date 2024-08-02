import os
import cantools
import argparse
from attribute_definitions import attribute_def_list

def add_attributes(file):
    db = cantools.database.load_file(file)
    print(f"Adding attributes to {file} ...")
    for message in db.messages:
        for attribute in attribute_def_list:
            if attribute.name not in message.dbc.attribute_definitions:
                message.dbc.attribute_definitions[attribute.name] = attribute
        break
    cantools.database.dump_file(db, file)
    print(f"   ...success!")

def process_files(path):
    if os.path.isdir(path):
        files = filter(os.path.isfile, os.listdir(path))
        for file in files:
            if os.path.splitext(file)[1] == ".dbc":
                if os.access(file, os.W_OK) and os.access(file, os.R_OK):
                    add_attributes(os.path.join(path, file))
    elif os.path.isfile(path) and os.path.splitext(path)[1].lower() == ".dbc":
        if os.access(path, os.W_OK) and os.access(path, os.R_OK):
            add_attributes(path)
    else:
        print(f"Invalid path! {path}")

def main():
    parser = argparse.ArgumentParser(description="Add attributes to DBC files.")
    parser.add_argument("path", nargs="?", default=os.curdir, help="Path to a directory or a DBC file. Default is current directory")
    args = parser.parse_args()

    if args.path == "?":
        parser.print_help()
    else:
        process_files(args.path)

if __name__ == "__main__":
    main()

