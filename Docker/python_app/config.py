from decouple import config

configValue = {
    'host': '13.51.250.203',
    'user': config("DB_USER"),
    'password': config("DB_PASSWORD"),
    'database': 'car_db'
}
