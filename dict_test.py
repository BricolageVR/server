import pandas as pd
import numpy as np


def get_test_dict1():
    dict = {"contact": {"name": "shir", "type": "person"}, "messages": [{"name": "asaf", "text": "1", "time": "5:22 PM, 4/7/2016"},
                                                                        {"name": "shir", "text": "2", "time": "5:23 PM, 4/7/2016"},
                                                                        {"name": "asaf", "text": "3", "time": "5:33 PM, 4/7/2016"},
                                                                        {"name": "shir", "text": "4", "time": "5:34 PM, 4/7/2016"},
                                                                        {"name": "asaf", "text": "5", "time": "5:45 PM, 4/7/2016"},
                                                                        {"name": "shir", "text": "6", "time": "5:45 PM, 4/7/2016"},
                                                                        {"name": "asaf", "text": "7", "time": "5:45 PM, 4/7/2016"},
                                                                        {"name": "shir", "text": "8", "time": "6:03 PM, 4/7/2016"},
                                                                        {"name": "asaf", "text": "9", "time": "6:04 PM, 4/7/2016"},
                                                                        {"name": "shir", "text": "10", "time": "6:12 PM, 4/7/2016"},
                                                                        {"name": "asaf", "text": "11", "time": "6:22 PM, 4/7/2016"},
                                                                        {"name": "shir", "text": "12", "time": "6:23 PM, 4/7/2016"},
                                                                        {"name": "asaf", "text": "13", "time": "6:25 PM, 4/22/2016"},
                                                                        {"name": "shir", "text": "14", "time": "6:26 PM, 4/25/2016"},
                                                                        {"name": "asaf", "text": "15", "time": "7:56 PM, 5/3/2016"},
                                                                        {"name": "shir", "text": "16", "time": "8:44 PM, 5/6/2016"}]}
    return dict


def get_test_dict2():
    dict = {"contact": {"name": "erez", "type": "group"}, "messages": [{"name": "erez", "text": "1", "time": "5:22 PM, 4/7/2016"},
                                                                        {"name": "asaf", "text": "2", "time": "5:23 PM, 4/7/2016"},
                                                                        {"name": "asaf", "text": "3", "time": "5:33 PM, 4/7/2016"},
                                                                        {"name": "erez", "text": "4", "time": "5:34 PM, 4/7/2016"},
                                                                        {"name": "erez", "text": "5", "time": "5:45 PM, 4/7/2016"},
                                                                        {"name": "erez", "text": "6", "time": "5:45 PM, 4/7/2016"},
                                                                        {"name": "asaf", "text": "7", "time": "5:45 PM, 4/7/2016"},
                                                                        {"name": "asaf", "text": "8", "time": "6:03 PM, 4/7/2016"},
                                                                        {"name": "asaf", "text": "9", "time": "6:04 PM, 4/7/2016"},
                                                                        {"name": "erez", "text": "10", "time": "6:12 PM, 4/7/2016"},
                                                                        {"name": "asaf", "text": "11", "time": "6:22 PM, 4/7/2016"},
                                                                        {"name": "erez", "text": "12", "time": "6:23 PM, 4/7/2016"},
                                                                        {"name": "asaf", "text": "13", "time": "6:25 PM, 4/22/2016"},
                                                                        {"name": "erez", "text": "14", "time": "6:26 PM, 4/25/2016"}]}
    return dict


def get_test_dict3():
    dict = {"contact": {"name": "erez", "type": "person"}, "messages": [{"name": "asaf", "text": "hi moses!", "time": "5:22 "
                                                                                                                      "PM, 4/7/2016"},
                                                                        {"name": "erez", "text": "אה כושי שלי",
                                                                         "time": "5:23 PM, 4/7/2016"}]}
    return dict


def get_test_dict4():
    dict = {"contact": {"name": "neta", "type": "person"}, "messages": [{"name": "asaf", "text": "hi moses!", "time": "5:22 "
                                                                                                                      "PM, 4/7/2016"},
                                                                        {"name": "neta", "text": "אה כושי שלי",
                                                                         "time": "5:23 PM, 4/7/2016"}]}
    return dict


def get_test_dict5():
    dict = {"contact": {"name": "bricolage", "type": "group"}, "messages": [{"name": "asaf", "text": "hi moses!",
                                                                             "time": "5:22 "
                                                                                     "PM, 4/7/2016"},
                                                                            {"name": "moses", "text": "אה כושי שלי",
                                                                             "time": "5:23 PM, 4/7/2016"}]}
    return dict


def init_df():
    print("initializing the DB")
    mydf = pd.DataFrame(data=None, columns=["contactName", "contactType", "name", "text", "time"])
    mydf.contactType.astype('category', categories=["person", "group"])
    mydf.name.astype('category')
    return mydf


def append_df(data):
    global df
    contactName = data["contact"]["name"]
    contactType = data["contact"]["type"]
    for message in data["messages"]:
        name = message["name"]
        text = message["text"]
        df = df.append({'contactName': contactName, 'contactType': contactType, 'name': name, 'text': text,
                        'time': message["time"]}, ignore_index=True)
    # todo check about chronological consistency
    print(df.info)


def test_df():
    global df
    df.time = pd.to_datetime(df.time)
    df = df.sort_values('time', ascending=True)  # todo check

    #         todo call all of the DataAnalysisMethods
    last_chats_json = df.head(6).to_json(date_format='iso', double_precision=0, date_unit='s', orient='records')  # todo make param

    df_no_groups = df[df.contactType == 'person']

    closest_persons_json = df_no_groups.contactName.value_counts().head(150).to_json(date_format='iso', double_precision=0, date_unit='s',
                                                                                     orient='records')  # todo make param
    print(min(df.time).date())

df = init_df()
append_df(get_test_dict1())
append_df(get_test_dict2())
test_df()



# time_str = str(message["time"])  # todo remove- apparently not needed
# sep_index = time_str.find(",") # assuming the time filed is constant
# hour = time_str[:]
# date = time_str[sep_index + 2:]
# time = date + " " + hour

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