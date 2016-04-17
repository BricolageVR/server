import tornado.ioloop
import tornado.web
import json
import os
from cgi import parse_header
import pandas as pd


def init_db():
    print("initializing the DB")
    empty_df = pd.DataFrame(data=None, columns=["contactName", "contactType", "name", "text", "time"])
    empty_df.contactType.astype('category', categories=["person", "group"])
    empty_df.name.astype('category')
    return empty_df


class WhatsAppHandler(tornado.web.RequestHandler):
    def post(self):
        global df
        print("GetWhatsAppChat post handler")
        data_json = self.request.body
        content_type = self.request.headers.get('content-type', '')
        content_type, params = parse_header(content_type)
        if content_type.lower() != 'application/json':
            print("ERROR: not the right content")
        charset = params.get('charset', 'UTF8')
        data = json.loads(data_json.decode(charset))
        # print(data)
        contact_name = data["contact"]["name"]
        contact_type = data["contact"]["type"]
        for message in data["messages"]:
            name = message["name"]
            text = message["text"]

            df = df.append({'contact_name': contact_name, 'contact_type': contact_type, 'name': name, 'text': text,
                            'time': message["time"]}, ignore_index=True)
#             todo check about chronological consistency


class FinishedWhatsAppHandler(tornado.web.RequestHandler):
    def post(self):
        df.time = pd.to_datetime(df.time)
        df.sort_values('time', ascending=True)  # todo check

#         todo call all of the DataAnalysisMethods


class DataAnalysisMethods:
    @staticmethod
    def get_last_chats(number_of_chats):
        return df.head(number_of_chats).to_json(date_format='iso', double_precision=0, date_unit='s', orient='records')

    @staticmethod
    def get_closest_persons(number_of_persons):
        df_no_groups = df[df.contactType == 'person']
        return df_no_groups.contactName.value_counts().head(number_of_persons).to_json(date_format='iso', double_precision=0,
                                                                                       date_unit='s', orient='records')
#     todo consider creating the non groups df at the start


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
        (r"/chat", WhatsAppHandler),
        (r"/chatFinished", FinishedWhatsAppHandler),
        (r"/string", teststring),
        (r"/json", testjson),
    ], **settings)


if __name__ == "__main__":
    df = init_db()
    port = 8888
    app = make_app()
    app.listen(port)
    tornado.ioloop.IOLoop.current().start()
