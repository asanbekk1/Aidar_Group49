import sqlite3


conn = sqlite3.connect('students.db')
cursor = conn.cursor()

def get_cities():
    cursor.execute("SELECT id, title FROM cities")
    return cursor.fetchall()

def get_students_by_city(city_id):
    query = """
    SELECT students.first_name, students.last_name, countries.title AS country, cities.title AS city, cities.area
    FROM students
    JOIN cities ON students.city_id = cities.id
    JOIN countries ON cities.country_id = countries.id
    WHERE cities.id = ?
    """
    cursor.execute(query, (city_id,))
    return cursor.fetchall()

def main():
    while True:
        print("Вы можете отобразить список учеников по выбранному id города из перечня городов ниже, для выхода из программы введите 0:")

        cities = get_cities()
        for city in cities:
            print(f"{city[0]}: {city[1]}")

        city_id = int(input("Введите id города: "))

        if city_id == 0:
            print("Выход из программы.")
        else:
            students = get_students_by_city(city_id)
            if students:
                for student in students:
                    print(f"Имя: {student[0]}, Фамилия: {student[1]}, Страна: {student[2]}, Город: {student[3]}, Площадь города: {student[4]} км²")
            else:
                print("Студентов в этом городе нет.")

if __name__ == '__main__':
    main()

conn.close()






























































