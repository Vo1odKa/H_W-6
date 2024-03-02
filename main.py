import sqlite3
from faker import Faker
import random

fake = Faker()
db_path = "H_W_6.bd"

# Створення бази даних та відкриття підключення
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Створення таблиць
cursor.execute('''
    CREATE TABLE IF NOT EXISTS stud (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        s_name TEXT,
        age INTEGER,
        group_id INTEGER,
        FOREIGN KEY (group_id) REFERENCES groups(id)
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS groups (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS teachers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        s_name TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS subjects (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        teacher_id INTEGER,
        FOREIGN KEY (teacher_id) REFERENCES teachers(id)
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS marks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        stud_id INTEGER,
        subject_id INTEGER,
        mark INTEGER,
        created_date DATE,
        FOREIGN KEY (stud_id) REFERENCES stud(id),  -- Змінено тут
        FOREIGN KEY (subject_id) REFERENCES subjects(id)
    )
''')

# Генерація випадкових даних та заповнення таблиць
groups = ['Group A', 'Group B', 'Group C']
subjects = ['Math', 'Physics', 'Chemistry', 'Literature', 'History', 'Biology', 'Computer Science', 'Art']
teachers_count = 5
students_count = 50
marks_count = 20

conn.commit()

# Додавання груп
for group_name in groups:
    cursor.execute("INSERT INTO groups (name) VALUES (?)", (group_name,))

# Додавання викладачів
for _ in range(teachers_count):
    cursor.execute("INSERT INTO teachers (name, s_name) VALUES (?, ?)", (fake.first_name(), fake.last_name()))

# Додавання предметів
for subject_name in subjects:
    teacher_id = random.randint(1, teachers_count)
    cursor.execute("INSERT INTO subjects (name, teacher_id) VALUES (?, ?)", (subject_name, teacher_id))

# Додавання студентів
for _ in range(students_count):
    cursor.execute("INSERT INTO stud (name, s_name, age, group_id) VALUES (?, ?, ?, ?)",
                   (fake.first_name(), fake.last_name(), fake.random_int(min=18, max=25), random.randint(1, len(groups))))

# Додавання оцінок
for _ in range(marks_count):
    stud_id = random.randint(1, students_count)
    subject_id = random.randint(1, len(subjects))
    mark = random.randint(60, 100)
    created_date = fake.date_this_decade()
    cursor.execute("INSERT INTO marks (stud_id, subject_id, mark, created_date) VALUES (?, ?, ?, ?)",
                   (stud_id, subject_id, mark, created_date))

# Збереження змін та закриття підключення
conn.commit()
conn.close()
