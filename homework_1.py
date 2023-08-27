import sqlite3

with sqlite3.connect('first.db') as db:
    cursor = db.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS subjects (
        id_subject INTEGER PRIMARY KEY,
        subject_name TEXT,
        subject_description TEXT,
        hours INTEGER,
        semester_number INTEGER
    )
    ''')

    data = [
        (1, 'Фізична культура', 'Основи фізкультури', 70, 1),
        (2, 'Фізика', 'Основи фізики', 50, 2),
        (3, 'Математика', 'Основи математики', 60, 1),
        (4, 'Історія', 'Історія стародавнього світу', 80, 1),
        (5, 'Зарубіжна література', 'Світова література', 75, 2),
        (6, 'Трудове навчання', 'Основи трудового навчання', 70, 1),
        (7, 'Хімія', 'Основи хімії', 65, 1),
        (8, 'Біологія', 'Загальна біологія', 80, 2),
        (9, 'Географія', 'Основи географії', 55, 2),
        (10, 'Музика', 'Музичне мистецтво', 40, 1),
    ]

    insert = 'INSERT INTO subjects (id_subject, subject_name, subject_description, hours, semester_number) VALUES (?, ?, ?, ?, ?)'
    cursor.executemany(insert, data)

    cursor.execute('SELECT subject_name, semester_number FROM subjects')
    reading_data = cursor.fetchall()

    for row in reading_data:
        print(row)