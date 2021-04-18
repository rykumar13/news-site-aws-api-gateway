from flask import Flask, request, make_response, jsonify
import mysql.connector
from mysql.connector import Error
import creds

app = Flask(__name__)


@app.route('/')
def hello_world():
    if request.method == "OPTIONS":  # CORS preflight
        return _build_cors_prelight_response()
    elif request.method == "GET":
        if request.authorization and request.authorization.username == creds.username and request.authorization.password == creds.password:
            connection = create_connection()
            results = jsonify(get_data(connection)[0][0])
            return _corsify_actual_response(results)
        return _corsify_actual_response(make_response('Could not verify!', 401, {'WWW-Authentication': 'Basic realm="Login Required"'}))


def _build_cors_prelight_response():
    response = make_response()
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add('Access-Control-Allow-Headers', "*")
    response.headers.add('Access-Control-Allow-Methods', "*")
    return response


def _corsify_actual_response(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


# We only need this for local development.
if __name__ == '__main__':
    app.run()


def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host=creds.db_host,
            user=creds.db_user,
            passwd=creds.password,
            database=creds.db_database
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection


def get_data(connection):
    try:
        sql = "SELECT JSON_ARRAYAGG(JSON_OBJECT('Id', ID," \
              "'Date', ARTICLE_DATE," \
              "'Category', CATEGORY," \
              "'Website', WEBSITE," \
              "'Name', NAME," \
              "'Url', URL," \
              "'Brief', BRIEF," \
              "'Picture', PICTURE" \
              ")) " \
              "FROM NEWS_SITE;"
        cursor = connection.cursor()
        cursor.execute(sql)
        result_json = cursor.fetchall()
        return result_json
    except Error as e:
        print(f"The error '{e}' occurred")
