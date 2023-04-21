import connexion

app = connexion.App(__name__, specification_dir="./")
app.add_api("swagger.yml")

if __name__ == "__main__":
    app.run(host="13.50.245.236", port=8000, debug=True)