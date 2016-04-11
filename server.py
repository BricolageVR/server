__package__ = "typeIt"  # todo change

import tornado.ioloop
import tornado.web
import json
import os
from cgi import parse_header
import numpy as np
import pandas as pd

# todo remove
# from pymongo import MongoClient
# import subprocess

# todo remove
# def initMongoDB(): # check about termination
#     print("firing up the mongoDb server")
#     subprocess.Popen(['C:\\Program Files\\MongoDB\\Server\\3.2\\bin\\mongod',
#                       '--dbpath', 'C:\\Users\\Asaf\\Google Drive\\Steamer\\github\\server\\db'])
#     print("connecting the client tor the mongoDb server")
#     client = MongoClient()
#     db = client.mydb
#     collection = db.my_collection
#     # continue db creation- design needed


def InitDB():
    print("initializing the DB")
    df = pd.DataFrame()


class GetWhatsAppChat(tornado.web.RequestHandler):
    def post(self):
        print("GetWhatsAppChat post handler")
        data_json = self.request.body
        content_type = self.request.headers.get('content-type', '')
        content_type, params = parse_header(content_type)
        if content_type.lower() != 'application/json':
            print("ERROR: not the right content")
        charset = params.get('charset', 'UTF8')
        data = json.loads(data_json.decode(charset))
        # print(data)
        contactName = data["contact"]["name"]
        contactType = data["contact"]["type"]
        for message in data["messages"]:
            name = message["name"]
            text = message["text"]
            time = message["time"]
            df = df.append({'contactName': contactName, 'contactType': contactType, 'name': name, 'text': text,
                            'time': time}, ignore_index=True)  # todo insert time as a time series


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        print("main.html")
        self.render("main.html")


class teststring(tornado.web.RequestHandler):
    def get(self):
        print("result handler")
        self.finish("this is a test line")


class testjson(tornado.web.RequestHandler):
    # def get(self):
    #     print("result handler")
    #     contacts = ["Erez Levanon", "Rotem Arbiv", "Neta Mozes", "Asaf Etzion"]
    #     result = {"contacts": contacts}
    #     result = json.dumps(result)
    #     self.finish(result)

    def post(self):
        print("testjson handler")
        data_json = self.request.body
        content_type = self.request.headers.get('content-type', '')
        content_type, params = parse_header(content_type)
        if content_type.lower() != 'application/json':
            print("ERROR: not the right content")

        charset = params.get('charset', 'UTF8')
        data = json.loads(data_json.decode(charset))
        print(data)


settings = dict(
    static_path=os.path.join(os.path.dirname(__file__), "static")
)


def make_app():
    print("make_app")
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/string", teststring),
        (r"/json", testjson),
    ], **settings)


if __name__ == "__main__":
    InitDB()
    port = 8888
    app = make_app()
    app.listen(port)
    tornado.ioloop.IOLoop.current().start()
