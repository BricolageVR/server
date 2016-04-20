import tornado.ioloop
import tornado.web
import json
import os
from cgi import parse_header
import pandas as pd
from pandas.tseries.frequencies import to_offset
from datetime import date, datetime


def init_df():
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

            df = df.append({'contactName': contact_name, 'contactType': contact_type, 'name': name, 'text': text,
                            'time': message["time"]}, ignore_index=True)
#             todo check about chronological consistency


class FinishedWhatsAppHandler(tornado.web.RequestHandler):

    def post(self):  # todo change app post to not send data
        print("FinishedWhatsAppHandler")
        global df
        global df_no_groups
        global user_name

        df.time = pd.to_datetime(df.time)
        df.sort_values('time', ascending=True)

        df_no_groups = df[df.contactType == 'person']


#         todo call all of the DataAnalysisMethods


class DataAnalysisMethods:
    global df_no_groups
    global df

    # returns the last number_of_chats with name, text and time
    @staticmethod
    def get_last_chats(number_of_chats):
        return df.head(number_of_chats).to_json(date_format='iso', double_precision=0, date_unit='s', orient='records')
        # todo return only hour or date if not today

    # gets a contact that the user talked to a lot in the past
    @staticmethod
    def get_blast_from_the_past(past_fraction):
        past_chats_threshold_days = past_fraction * (
            pd.Timestamp(date(datetime.today().year, datetime.today().month, datetime.today().day)).date() - (
                         min(df_no_groups.time).date()))
        past_chats_threshold_date = min(df_no_groups.time) + to_offset(past_chats_threshold_days)
        print(past_chats_threshold_date)
        df_past_chats = df_no_groups.where(df_no_groups.time <= past_chats_threshold_date).dropna()
        return df_past_chats.contactName.value_counts().head(1).index[0]

    # finds the number_of_persons most talked persons and a message that has the user name in it.
    @staticmethod
    def get_closest_persons_and_msg(number_of_persons, user_name, past_fraction_param):
        closest_persons_ndarray = df_no_groups.contactName.value_counts().head(number_of_persons).index
        i = 0
        closest_persons_df = pd.DataFrame()
        for contactName in closest_persons_ndarray:
            closest_persons_df = closest_persons_df.append({'contactName': contactName, 'text': user_name}, ignore_index=True)
            for index, col in df_no_groups.iterrows():
                if col['contactName'] == contactName:
                    if 'asaf' in col['text']:
                        closest_persons_df.iloc[i].text = col['text']
            i += 1

        blast = DataAnalysisMethods.get_blast_from_the_past(past_fraction_param)
        closest_persons_df = closest_persons_df.append({"contactName": blast, "text": "im the blast fron the past"}, ignore_index=True)
        return closest_persons_df.to_json(date_format='iso', double_precision=0, date_unit='s', orient='records')

    @staticmethod
    def get_good_night_messages():
        good_night_df = df_no_groups[df_no_groups.text.str.contains("good night|לילה טוב|bonne nuit|sweet dreams|ליל מנוחה")]
        good_night_df = good_night_df[['contactName', 'text']]
        return good_night_df.to_json(date_format='iso', double_precision=0, date_unit='s', orient='records')

    @staticmethod
    def get_dream_messages():
        good_night_df = df_no_groups[df_no_groups.text.str.contains(
            "חלמתי|חלומות|חלמת|dream|dreamt|dreaming|dreams|rêver|rêves|rêvé|rêve|reve|reves|rever|dreamed")]
        good_night_df = good_night_df[['contactName', 'text']]
        return good_night_df

    # @staticmethod
    # def get_old_messages(past_fraction): # todo complete
        # past_chats_threshold_days = past_fraction * (
        #     pd.Timestamp(date(datetime.today().year, datetime.today().month, datetime.today().day)).date() - (
        #         min(df_no_groups.time).date()))
        # past_chats_threshold_date = min(df_no_groups.time) + to_offset(past_chats_threshold_days)
        # print(past_chats_threshold_date)
        # df_past_chats = df_no_groups.where(df_no_groups.time <= past_chats_threshold_date).dropna()
        # return df_past_chats.contactName.value_counts().head(1).index[0]


    @staticmethod
    def get_dreams_or_old_messages():
        dreams_df = DataAnalysisMethods.get_dream_messages()

        num_of_sentences = 0
        for text in dreams_df.text:
            if len(text.strip().split()) > 2:
                num_of_sentences += 1

        if num_of_sentences >= 5:
            return dreams_df.to_json(date_format='iso', double_precision=0, date_unit='s', orient='records')
        else:
            return



class MainHandler(tornado.web.RequestHandler):
    def get(self):
        print("main.html")
        self.render("main.html")


class teststring(tornado.web.RequestHandler):
    def get(self):
        print("result handler")
        self.finish("this is a test line")


class UserNameHandler(tornado.web.RequestHandler):
    # def get(self):
    #     print("result handler")
    #     contacts = ["Erez Levanon", "Rotem Arbiv", "Neta Mozes", "Asaf Etzion"]
    #     result = {"contacts": contacts}
    #     result = json.dumps(result)
    #     self.finish(result)

    def post(self):
        global user_name
        print("UserNameHandler")
        data_json = self.request.body
        content_type = self.request.headers.get('content-type', '')
        content_type, params = parse_header(content_type)
        if content_type.lower() != 'application/json':
            print("ERROR: not the right content")

        charset = params.get('charset', 'UTF8')
        data = json.loads(data_json.decode(charset))
        print("the user name is: " + data['userName'])
        user_name = data['userName']


settings = dict(
    static_path=os.path.join(os.path.dirname(__file__), "static")
)


def make_app():
    print("make_app")
    return tornado.web.Application([
        (r"/", MainHandler),  # todo remove
        (r"/userName", UserNameHandler),
        (r"/chat", WhatsAppHandler),
        (r"/chatFinished", FinishedWhatsAppHandler),
        (r"/string", teststring),  # todo remove
        # (r"/json", UserNameHandler),  # todo remove
    ], **settings)


if __name__ == "__main__":
    df = init_df()
    df_no_groups = pd.DataFrame()
    user_name = ""
    port = 8888
    app = make_app()
    app.listen(port)
    tornado.ioloop.IOLoop.current().start()
