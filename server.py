__package__ = "typeIt"

import tornado.ioloop
import tornado.web
import json
import os
from platform import system

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        print("main.html")
        self.render("main.html")

class searchHandler(tornado.web.RequestHandler):
    def post(self):
        print("search handler")
        body = bytes.decode(self.request.body)
        body = json.loads(body)
        msg = body["msg"]
        timestamp = body["time"]
        uid = body["id"]
        if msg != "":
            try:
                test_result = predictor.test_result(msg, timestamp, uid)
                print(test_result)
                result = {"result":[test_result]}
                result = json.dumps(result)
            except KeyError:
                self.set_status(404)
                result = "no such user id"
        else:
            self.set_status(404)
            result = json.dumps("empy message")
        self.finish(result)
        print('sent result')

class teststring(tornado.web.RequestHandler):
    def get(self):
        print("result handler")
        self.finish("this is a test line")

class testjson(tornado.web.RequestHandler):
    def get(self):
        print("result handler")
        contacts = ["Erez Levanon", "Rotem Arbiv", "Neta Mozes", "Asaf Etzion"]
        result = {"contacts":contacts}
        result = json.dumps(result)
        self.finish(result)

settings = dict(
    static_path = os.path.join(os.path.dirname(__file__), "static")
)

def make_app():
    print("make_app")
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/string", teststring),
        (r"/json", testjson),
    ], **settings)


if __name__ == "__main__":
    port = 8888
    app = make_app()
    app.listen(port)
    tornado.ioloop.IOLoop.current().start()
