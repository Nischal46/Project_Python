import sqlite3



try:
    conn = sqlite3.connect('student.db', detect_types=sqlite3.PARSE_DECLTYPES)
    conn.row_factory = sqlite3.Row
    db = conn.cursor()

    db.execute('''
    CREATE TABLE IF NOT EXISTS students (
           id INTEGER PRIMARY KEY AUTOINCREMENT,
           name TEXT NOT NULL,
           email TEXT NOT NULL,
           contact TEXT NOT NULL
    )
    ''')

    def add_student(student_name, student_email, student_contact):
        db.execute("INSERT INTO students (name, email, contact) VALUES (?, ?, ?)", (student_name, student_email, student_contact))
        conn.commit()

    def get_all_student_details():
        db.execute("SELECT * FROM students")
        rows = db.fetchall()
        st_array = []
        for student_row in rows:
        # Convert the row to a dictionary for easier access
            student_dict = dict(student_row)
            st_array.append(student_dict)
        print(st_array)
    
except sqlite3.Error as e:
    print("An error occurred:", e.args[0])


def main():
    bool = True

    while bool:
        print('''
            Press 1 to add the student details
            Press 2 to update the student details
            Press 3 to delete the student details
            Press 4 to get all the student details
            Press 5 to get single details by id
            Press 6 to exit the app
            ''')
        
        choice = int(input("Enter a choice: "))

        match choice:
            case 1:
                st_name = input("Enter student name: ")
                st_email = input("Enter student email: ")
                st_contact = input("Enter student contact: ")
                add_student(st_name, st_email, st_contact)

            case 4:
                get_all_student_details()

            case _:
                print('Invalid input choice.Please use correct choice.')

    conn.close()

            
                

if __name__ == "__main__":
    main()
