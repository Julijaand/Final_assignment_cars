from decouple import config

configValue = {
    'host':"localhost",
    'user': config("username"), 
    'password': config("password"), 
    'database': 'car_db'
}