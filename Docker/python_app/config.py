from decouple import config

configValue = {
    'host': '13.50.245.236',
    'user': config("DB_USER"),
    'password': config("DB_PASSWORD"),
    'database': 'car_db'
}