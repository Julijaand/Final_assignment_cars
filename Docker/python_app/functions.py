from Docker.python_app import db_connect as db

def get_all_cars():
    car_list = []
    with db.crete_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT brand, model, year, colour, price FROM cars")
            for car in cursor.fetchall():
                car_dict = {
                    'brand': car[0],
                    'model': car[1],
                    'year': car[2],
                    'colour': car[3],
                    'price': car[4],
                }
                car_list.append(car_dict)
    return car_list


def create_new_car(car):
    existing_car = get_one_car(car['brand'])
    if existing_car:
        return {'error': f"Car with name {car['brand']} already exists"}, 409

    with db.create_connection() as connection:
        with connection.cursor() as cursor:
            query = "INSERT INTO cars (brand, model, year, colour, price) VALUES (%s, %s, %d, %s, %d);"
            values = (car['brand'], car['model'], car['year'], car['colour'], car['price'])
            cursor.execute(query, values)
            connection.commit()
    return car, 201


def get_one_car(brand):
    with db.crete_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT brand, model, year, colour, price FROM cars WHERE brand ='" + brand + "'")
            car = cursor.fetchone()
            if car is not None:
                return {
                    'brand': car[0],
                    'model': car[1],
                    'year': car[2],
                    'colour': car[3],
                    'price': car[4],
                }
            else:
                return None


def delete_car(brand):
    with db.crete_connection() as conn:
        with conn.cursor() as cursor:
            delete_query = "DELETE FROM cars WHERE brand ='" + brand + "'"
            cursor.execute(delete_query)
            conn.commit()
            return cursor.rowcount


def update_car(brand, car):
    with db.crete_connection() as conn:
        with conn.cursor() as cursor:
            update_query = "UPDATE cars SET brand = %s, model = %s, year = %d, colour = %s, price = %d WHERE brand = %s"
            values = (car['model'], car['year'], car['colour'], car['price'], brand)
            cursor.execute(update_query, values)
            conn.commit()
        return car
