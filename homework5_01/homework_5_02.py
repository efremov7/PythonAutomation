people_records = [
    ('John', 'Doe', 28, 'Engineer', 'New York'),
    ('Alice', 'Smith', 35, 'Teacher', 'Los Angeles'),
    ('Bob', 'Johnson', 45, 'Doctor', 'Chicago'),
    ('Emily', 'Williams', 30, 'Artist', 'San Francisco'),
    ('Michael', 'Brown', 22, 'Student', 'Seattle'),
    ('Sophia', 'Davis', 40, 'Lawyer', 'Boston'),
    ('David', 'Miller', 33, 'Software Developer', 'Austin'),
    ('Olivia', 'Wilson', 27, 'Marketing Specialist', 'Denver'),
    ('Daniel', 'Taylor', 38, 'Architect', 'Portland'),
    ('Grace', 'Moore', 25, 'Graphic Designer', 'Miami'),
    ('Samuel', 'Jones', 50, 'Business Consultant', 'Atlanta'),
    ('Emma', 'Hall', 31, 'Chef', 'Dallas'),
    ('William', 'Clark', 29, 'Financial Analyst', 'Houston'),
    ('Ava', 'White', 42, 'Journalist', 'San Diego'),
    ('Ethan', 'Anderson', 36, 'Product Manager', 'Phoenix')
]


my_record = ('Mike', 'Efremov', 25, 'Test Engineer', 'Odessa')
people_records.insert(0, my_record)

print("Список після додавання:")
for index, person in enumerate(people_records):
    print(f"  [{index}] {person}")


people_records[1], people_records[5] = people_records[5], people_records[1]

print("\n2. Після swap індексів 1 <-> 5:")
for index, person in enumerate(people_records):
    marker = " <<<" if index in (1, 5) else ""
    print(f"  [{index}] {person}{marker}")


indexes_to_check = [6, 10, 13]
result = all(people_records[i][2] >= 30 for i in indexes_to_check)

print("\n3. Перевірка віку (>= 30) для індексів 6, 10, 13:")
for index in indexes_to_check:
    person = people_records[index]
    print(f"  [{index}] {person[0]} {person[1]}, вік: {person[2]} — {'Yes' if person[2] >= 30 else 'NO'}")

print(f"\n  Всі мають вік >= 30: {result}")