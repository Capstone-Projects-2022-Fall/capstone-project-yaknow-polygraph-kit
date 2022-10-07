# import
import PySimpleGUI as gui

database = ['']

def read_database_file():
    with open('database.txt') as f:
        for questions in f.readlines():
            database.append(questions.split())

    return database


def main():
    result = read_database_file()
    print(result)


if __name__ == '__main__':
    main()