import sqlite3

def create_connection(): # --> Database-i yaratmaq ucun
    conn = sqlite3.connect('../Student.db')
    cursor = conn.cursor()
    return conn, cursor

def create_table(cursor): # --> Table yaratmaq ucun
    # IF NOT EXISTS --> 2ci defe run edildikde error vermemesi ucun
    cursor.execute('''CREATE TABLE IF NOT EXISTS Students1 (
    id INTEGER PRIMARY KEY ,
    name TEXT NOT NULL,
    surname TEXT NOT NULL,
    adress TEXT NOT NULL,
    email TEXT NOT NULL,
    price INTEGER NOT NULL
    )''')

def insert_student(cursor): # Value-lari elave etmek ucun
    students = [
    (1,"Babak","Alizada","Baku","babakalizada@gmail.com",2200),
    (2,"Nihad","Mammadli","Absheron","nihadmemmedli@gmail.com",2100),
    (3,"Fegan","Guliyev","Lokbatan","feganguliyev@gmail.com",2150),
    (4,"Shakir","Abilov","Baku","shakirabilov@gmail.com",2100),
    (5, "Elmir","Aliyev","Sumgayit","elmiraliyev@gmail.com",1800),
    (6, "Suleyman", "Memmedov","Absheron","suleymanmemmedov@gmail.com",1950)
    ]
    # INSERT OR IGNORE --> 2ci defe run edildikde error vermemesi ucun
    cursor.executemany("INSERT OR IGNORE INTO Students1 VALUES (?,?,?,?,?,?)", students)

def basic_SQL_operation(cursor): # --> Table-daki butun value-lari gostermek ucun
    cursor.execute("SELECT * FROM Students1")
    result = cursor.fetchall()
    for row in result:
        print(f'ID: {row[0]} | Name: {row[1]} | Surname: {row[2]} | Address: {row[3]} | Email: {row[4]} | Price: {row[5]}')

def add_new_row(cursor):
    print("Are You Add New Info to Students Table? Y/N")
    AskUser = input("Answer:")
    if AskUser == "Y":
        # Məlumatları alırıq
        new_id = int(input("Enter ID: "))
        name = input("Enter Name: ")
        surname = input("Enter Surname: ")
        address = input("Enter Address: ")
        email = input("Enter Email: ")
        price = int(input("Enter Price: "))

        NewList = [new_id, name, surname, address, email, price]

        # SQL əmrini yalnız istifadəçi məlumat daxil etdikdə icra edirik
        cursor.execute("INSERT INTO Students1 VALUES (?,?,?,?,?, ?)", NewList)
        print("Məlumat uğurla əlavə edildi!")
    else:
        print("Yeni məlumat əlavə edilmədi.")

def main():
    conn, cursor = create_connection()
    try:
        create_table(cursor)
        insert_student(cursor)
        basic_SQL_operation(cursor)
        add_new_row(cursor)
        conn.commit()
    except sqlite3.Error as e:
        print("SQLite error:", e)
    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    main()
