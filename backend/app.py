from flask import Flask
import mysql.connector

app = Flask(__name__)

@app.route('/data')
def data():
    try:
        conn = mysql.connector.connect(
            host="RDS-ENDPOINT",
            user="admin",
            password="password",
            database="mydb"
        )
        return "DB connection successful!"
    except Exception as e:
        return str(e)

app.run(host='0.0.0.0', port=8000)
