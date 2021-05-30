from pymongo import MongoClient, errors
from flask import Flask, jsonify, abort, request
from telegram_my import TelegramMy
import os
from dotenv import load_dotenv
import traceback

DOMAIN = '0.0.0.0'
# DOMAIN = '172.17.0.3'
PORT = 27017

app = Flask(__name__)
log = ''


@app.route('/', methods=['GET'])
def i_am_alive():
    return 'I am alive! <br><a href="mongo">Try MongoDB</a>'


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return '404'


@app.errorhandler(500)
def page_not_found(e):
    # note that we set the 404 status explicitly
    # teleg.send(str(log))
    return f'500 {str(e)}\n{log}'


@app.route('/mongo', methods=['GET'])
def mongo():
    global log
    log = ''
    try:
        client = MongoClient(
            host=[DOMAIN + ":" + str(PORT)],
            serverSelectionTimeoutMS=3000,
            username="root",
            password="1234",
        )

        db = client.demoDB

        collection = db.demoCollection

        document1 = {
            "name": "John",
            "age": 24,
            "location": "New York"
        }

        document2 = {
            "name": "Sam",
            "age": 21,
            "location": "Chicago"
        }

        collection.insert_one(document1)
        collection.insert_one(document2)

        cursor = collection.find()
        strr = 'OK'
        for record in cursor:
            print(record)
            strr = f'{str}\n{str(record)}'

        return strr

        # log = f'{log} 1'
        #
        # # print("version:", client.server_info()["version"])
        # # log = f'{log} 2'
        #
        # teleg.send(str(client.server_info()))
        #
        # database_names = client.list_database_names()
        # log = f'{log} 3'
        # print("OK:", database_names)
        # strr

    except errors.ServerSelectionTimeoutError as err:
        print("pymongo ERROR:", err)
        return f'error: {str(err)}'

    except Exception as ex:
        message = f'ERROR: {str(ex)}'
        # teleg.send(message)
        ex_test = traceback.format_exc()
        # teleg.send_text_as_file(ex_test)
        # raise ex
        return f'{str(message)}'


if __name__ == '__main__':
    # app.run(debug=True, port=8080)
    # app.run(debug=True)
    # load_dotenv()
    # teleg = TelegramMy(os.getenv('TELEGRAMTOKEN'), os.getenv('CHATID'))
    # teleg.set_project_prefix('py+mongo')
    # teleg.send('test')

    app.run(host='0.0.0.0', port=8080)
