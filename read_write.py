import os
import sys

bundle_dir = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))
path = os.path.abspath(os.path.join(bundle_dir, 'database.txt'))

def read_database_file():
    local_database = []
    with open(path) as f:
        for questions in f.readlines():
            local_database.append(questions.strip('\n'))
    return local_database

def create_question(question):
    local_question = question.lower()
    local_database = read_database_file()

    for questions in range(len(local_database)):
        local_database[questions] = local_database[questions].lower()

    if local_question not in local_database:
        f = open(path, 'a')
        f.write("\n" + question.capitalize())
        f.close()
        local_database.append(local_question)
        local_database.append(question)
        print("Your Question " + "( " + question.capitalize() + " )" + " Was Successfully Added")
        return local_database
    else:
        return "Your Question " + "( " + question.capitalize() + " )" + " Already Exists"


def read_question(question):
    local_question = question.lower()
    local_database = read_database_file()

    for questions in range(len(local_database)):
        local_database[questions] = local_database[questions].lower()

    if local_question not in local_database:
        return "Your Question " + "( " + question.capitalize() + " )" + " Not Found In Database"
    else:
        return "Your Question " + "( " + question.capitalize() + " )" + " Found In Database"

def main():
    print(read_database_file())
    print(create_question("What Is Your Name?"))
    print(read_question("What Is Your Name?"))

if __name__ == "__main__":
    main()