from decouple import config

configValue = {
    'host': 'mysql',
    'user': config("DB_USER"),
    'password': config("DB_PASSWORD"),
    'database': 'car_db'
}
