import functions as f
from flask import make_response

def read_all():
    return f.get_all_cars(), 200

def create_car(car):
    car, status_code = f.create_new_car(car)
    return car, status_code

def read_one_car(name):
    return f.get_one_car(name), 200

def delete_car(name):
    rows_affected = f.delete_car(name)

    if rows_affected > 0:
        return make_response(f"{name} successfully deleted", 200)
    else:
        return make_response(f"Deletion of {name} failed. Car not found.", 404)


def update_car(name, car):
    return f.update_car(name, car), 200
