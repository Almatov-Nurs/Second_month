# откоментируйте желаемую функцию
import sqlite3

database_2 = sqlite3.connect("server1.sqlite3")

curs = database_2.cursor()

curs.execute(
    """CREATE TABLE IF NOT EXISTS note (
    note TEXT,
    answer TEXT
    )
    """
)

database_2.commit()

def add_notes(): # функция для добвления заметки
    global user_note
    user_note = input("Ваша заметка: ")

    curs.execute(f"SELECT note FROM note WHERE note = '{user_note}'")
    if curs.fetchone() is None:
        curs.execute("INSERT INTO note VALUES (?,?)",(user_note,"нет")) # 'нет' значит заметка не выполнена
        database_2.commit()                                             # по дефолту при создании оно остается не выполненным
        print('вы добавили заметку!')
        for i in curs.execute("SELECT * FROM note"):
            print(i)
    else:
        for i in curs.execute("SELECT * FROM note"):
            print(i)
        print('такая заметка уже существует!')

# add_notes()

def question(): # тут кароче вычеркиваешь заметку из личных дел, то есть отвечаешь да или нет 
    global choose, ans
    print('-'*40,'\nвсе ваши заметки:')
    for i in curs.execute("SELECT * FROM note"):
        print(i)
    choose = input("выберите заметку: ")

    curs.execute(f"SELECT note FROM note WHERE note = '{choose}'")
    if curs.fetchone():
        while 1:                                                  # строго да или нет
            ans = input("Выполнено?(да,нет) : ")
            if ans != 'да' and ans != 'нет':
                print('вводите только да или нет!')
                continue
            else:
                break
        if ans == 'да':
            curs.execute(f"DELETE FROM note WHERE note = '{choose}'")
            database_2.commit()
            print("заметка удалена из списка дел!")
        for i in curs.execute("SELECT * FROM note"):
            print(i)
    else:
        print('такая заметка не существует!')

# question()
