import pandas as pd
from pandas.tseries.frequencies import to_offset
import numpy as np
from datetime import date, datetime


def get_test_dict1():
    dict = {"contact": {"name": "shir", "type": "person"}, "messages": [{"name": "me", "text": "text1", "time": "5:22 PM, 4/7/2014"},
                                                                        {"name": "shir", "text": "text2", "time": "5:23 PM, 4/7/2014"},
                                                                        {"name": "asaf", "text": "text3ה", "time": "5:33 PM, 4/7/2014"},
                                                                        {"name": "shir", "text": "text4", "time": "5:34 PM, 4/7/2014"},
                                                                        {"name": "asaf", "text": "text5", "time": "5:45 PM, 4/7/2014"},
                                                                        {"name": "shir", "text": "text6", "time": "5:45 PM, 4/7/2015"},
                                                                        {"name": "asaf", "text": "text7", "time": "5:45 PM, 4/7/2016"},
                                                                        {"name": "shir", "text": "text8", "time": "6:03 PM, 4/7/2016"},
                                                                        {"name": "asaf", "text": "text9", "time": "6:04 PM, 4/7/2016"},
                                                                        {"name": "shir", "text": "text10", "time": "6:12 PM, 4/7/2016"},
                                                                        {"name": "asaf", "text": "text11", "time": "6:22 PM, 4/7/2016"},
                                                                        {"name": "shir", "text": "asלילה טוב12as כע גכע", "time": "6:23 "
                                                                                                                                  "PM, "
                                                                                                                        "4/7/2016"},
                                                                        {"name": "asaf", "text": "text13", "time": "6:25 PM, 4/22/2016"},
                                                                        {"name": "shir", "text": "text14", "time": "6:26 PM, 4/25/2016"},
                                                                        {"name": "asaf", "text": "good night text15", "time": "7:56 PM, "
                                                                                                                        "5/3/2016"},
                                                                        {"name": "shir", "text": "text16", "time": "8:44 PM, 5/6/2016"}]}
    return dict


def get_test_dict2():
    dict = {"contact": {"name": "bricolage", "type": "group"}, "messages": [{"name": "erez", "text": "text1", "time": "5:22 PM, 4/7/2014"},
                                                                        {"name": "asaf", "text": "text2", "time": "5:23 PM, 4/7/2014"},
                                                                        {"name": "asaf", "text": "text3", "time": "5:33 PM, 4/7/2016"},
                                                                        {"name": "asaf", "text": "text4", "time": "5:34 PM, 4/7/2016"},
                                                                        {"name": "erez", "text": "text5", "time": "5:45 PM, 4/7/2016"},
                                                                        {"name": "erez", "text": "asaf6", "time": "5:45 PM, 4/7/2016"},
                                                                        {"name": "asaf", "text": "text7", "time": "5:45 PM, 4/7/2016"},
                                                                        {"name": "asaf", "text": "text8", "time": "6:03 PM, 4/7/2016"},
                                                                        {"name": "yuval", "text": "text9", "time": "6:04 PM, 4/7/2016"},
                                                                        {"name": "yuval", "text": "text10", "time": "6:12 PM, 4/7/2016"},
                                                                        {"name": "yuval", "text": "text11", "time": "6:22 PM, 4/7/2016"},
                                                                        {"name": "yuval", "text": "text12", "time": "6:23 PM, 4/7/2016"},
                                                                        {"name": "yuval", "text": "text13", "time": "6:25 PM, 4/22/2016"},
                                                                        {"name": "yuval", "text": "text14", "time": "6:26 PM, 4/25/2016"}]}
    return dict


def get_test_dict3():
    dict = {"contact": {"name": "yuval", "type": "person"}, "messages": [{"name": "asaf", "text": "text1", "time": "5:22 PM, 4/7/2014"},
                                                                        {"name": "yuval", "text": "text2", "time": "5:23 PM, 4/7/2014"},
                                                                        {"name": "yuval", "text": "text3", "time": "5:33 PM, 4/7/2014"},
                                                                        {"name": "yuval", "text": "text4", "time": "5:34 PM, 4/7/2014"},
                                                                        {"name": "yuval", "text": "text5", "time": "5:45 PM, 4/7/2014"},
                                                                        {"name": "yuval", "text": "text6", "time": "5:45 PM, 4/7/2015"},
                                                                        {"name": "asaf", "text": "text7", "time": "5:45 PM, 4/7/2015"},
                                                                        {"name": "yuval", "text": "text8", "time": "6:03 PM, 4/7/2015"},
                                                                        {"name": "asaf", "text": "good night 121", "time": "6:04 PM, "
                                                                                                                        "4/7/2015"},
                                                                        {"name": "yuval", "text": "text10", "time": "6:12 PM, 4/7/2016"},
                                                                        {"name": "asaf", "text": "text11", "time": "6:22 PM, 4/7/2016"},
                                                                        {"name": "yuval", "text": "text12", "time": "6:23 PM, 4/7/2016"},
                                                                        {"name": "asaf", "text": "text13", "time": "6:25 PM, 4/22/2016"},
                                                                        {"name": "yuval", "text": "לילה טוב", "time": "6:26 PM, "
                                                                                                                      "4/25/2016"}]}
    return dict


def get_test_dict4():
    dict = {"contact": {"name": "grega", "type": "group"}, "messages": [{"name": "erez", "text": "text1", "time": "5:22 PM, 4/7/2014"},
                                                                            {"name": "asaf", "text": "text2", "time": "5:23 PM, 4/7/2014"},
                                                                            {"name": "asaf", "text": "text3", "time": "5:33 PM, 4/7/2016"},
                                                                            {"name": "yuval", "text": "text4", "time": "5:34 PM, 4/7/2016"},
                                                                            {"name": "yuval", "text": "text5", "time": "5:45 PM, 4/7/2016"},
                                                                            {"name": "yuval", "text": "asaf6", "time": "5:45 PM, 4/7/2016"},
                                                                            {"name": "yuval", "text": "text7", "time": "5:45 PM, 4/7/2016"},
                                                                            {"name": "asaf", "text": "text8", "time": "6:03 PM, 4/7/2016"},
                                                                            {"name": "yuval", "text": "text9", "time": "6:04 PM, 4/7/2016"}]}
    return dict


def get_test_dict5():
    dict = {"contact": {"name": "family", "type": "group"}, "messages": [{"name": "erez", "text": "text1", "time": "5:22 PM, 4/7/2014"},
                                                                            {"name": "asaf", "text": "text2", "time": "5:23 PM, 4/7/2014"},
                                                                            {"name": "asaf", "text": "text3", "time": "5:33 PM, 4/7/2016"},
                                                                            {"name": "yuval", "text": "text4", "time": "5:34 PM, 4/7/2016"},
                                                                            {"name": "yuval", "text": "text5", "time": "5:45 PM, 4/7/2016"},
                                                                            {"name": "yuval", "text": "asaf6", "time": "5:45 PM, 4/7/2016"},
                                                                            {"name": "asaf", "text": "text7", "time": "5:45 PM, 4/7/2016"},
                                                                            {"name": "asaf", "text": "text8", "time": "6:03 PM, 4/7/2016"},
                                                                         {"name": "asaf", "text": "text8", "time": "6:03 PM, 4/7/2016"},
                                                                         {"name": "asaf", "text": "text8", "time": "6:03 PM, 4/7/2016"},
                                                                         {"name": "asaf", "text": "text8", "time": "6:03 PM, 4/7/2016"},
                                                                         {"name": "asaf", "text": "text8", "time": "6:03 PM, 4/7/2016"},
                                                                         {"name": "asaf", "text": "text8", "time": "6:03 PM, 4/7/2016"},
                                                                         {"name": "asaf", "text": "text8", "time": "6:03 PM, 4/7/2016"},
                                                                         {"name": "asaf", "text": "text8", "time": "6:03 PM, 4/7/2016"},
                                                                            {"name": "yuval", "text": "text9", "time": "6:04 PM, 4/7/2016"},
                                                                            {"name": "erez", "text": "text10", "time": "6:12 PM, 4/7/2016"},
                                                                            {"name": "asaf", "text": "text11", "time": "6:22 PM, "
                                                                                                                       "4/7/2016"}]}
    return dict


def init_df():
    print("initializing the DB")
    mydf = pd.DataFrame(data=None, columns=["contactName", "contactType", "name", "text", "time"])
    mydf.contactType.astype('category', categories=["person", "group"])
    mydf.name.astype('category')
    mydf.text.astype('str')
    return mydf


def append_df(data):
    print("started appending the data")
    global df
    contactName = data["contact"]["name"]
    contactType = data["contact"]["type"]
    for message in data["messages"]:
        name = message["name"]
        text = message["text"]
        df = df.append({'contactName': contactName, 'contactType': contactType, 'name': name, 'text': text,
                        'time': message["time"]}, ignore_index=True)
    # todo check about chronological consistency
    # print(df.info)

def test_df():
    global df
    df.time = pd.to_datetime(df.time)
    df = df.sort_values('time', ascending=True)  # todo check

    #         todo call all of the DataAnalysisMethods
    last_chats_json = df.head(6).to_json(date_format='iso', double_precision=0, date_unit='s', orient='records')  # todo make param
    # print(last_chats_json)

    df_no_groups = df[df.contactType == 'person']
    df_groups = df[df.contactType == 'group']

    closest_persons_ndarray = df_no_groups.contactName.value_counts().head(150).index
    i = 0
    closest_persons_df = pd.DataFrame()
    for contactName in closest_persons_ndarray:
        closest_persons_df = closest_persons_df.append({'contactName': contactName, 'text': 'asaf'}, ignore_index=True)
        for index, col in df_no_groups.iterrows():
            if col['contactName'] == contactName:
                if 'asaf' in col['text']:
                    closest_persons_df.iloc[i].text = col['text']
        i += 1

    # print(closest_persons_df.to_json(date_format='iso', double_precision=0, date_unit='s', orient='records'))


    past_chats_threshold_days = 0.5 * (pd.Timestamp(date(datetime.today().year,  datetime.today().month,  datetime.today().day)).date() - (
        min(df_no_groups.time).date()))

    past_chats_threshold_date = min(df_no_groups.time) + to_offset(past_chats_threshold_days)
    # print(past_chats_threshold_date)
    df_past_chats = df_no_groups.where(df_no_groups.time <= past_chats_threshold_date).dropna()
    blast_from_the_past = df_past_chats.contactName.value_counts().head(1).index[0]
    closest_persons_df = closest_persons_df.append({"contactName":blast_from_the_past,"text":"im the blast fron the past"}, ignore_index=True)
    # print(closest_persons_df)


    good_night_df = df_no_groups[df_no_groups.text.str.contains("good night|לילה טוב|bonne nuit|sweet dreams|ללט|לילה נהדר|ליל מנוחה")]
    good_night_df = good_night_df[['contactName', 'text']]

    num_of_sentences = 0
    for text in good_night_df.text:
        if len(text.strip().split()) > 2:
            num_of_sentences += 1

    if num_of_sentences >= 5:
        return
 # print(good_night_df)

    past_chats_threshold_days = 0.25 * (
        pd.Timestamp(date(datetime.today().year, datetime.today().month, datetime.today().day)).date() - (
            min(df_no_groups.time).date()))
    past_chats_threshold_date = min(df_no_groups.time) + to_offset(past_chats_threshold_days)
    # print(past_chats_threshold_date)
    df_past_chats = df_no_groups.where(df_no_groups.time <= past_chats_threshold_date).dropna()
    # print(df_past_chats)

    def get_most_active_groups(max_number_of_groups):
        return list(df_groups['contactName'].value_counts().index)[:max_number_of_groups]

    def get_users_activity_in_group(group_df): # todo maybe make maximum number of users
        return list(group_df.name.value_counts().index)

    most_active_groups_list = get_most_active_groups(3)
    # print(most_active_groups_list)
    # for group_name in most_active_groups_list:
    #     get_most_active_groups(df_groups[df_groups["contactName"].all() == group_name])
    groups = df_groups.groupby('contactName')
    ret_dict_list = []
    i = 0
    for group_name in most_active_groups_list:
        for name, group in groups:
            if name is group_name:
                ret_dict_list.append({})
                ret_dict_list[i]["groupName"] = name
                # print(ret_dict_list[i]["groupName"])

                ret_dict_list[i]["groupContacts"] = get_users_activity_in_group(group)
                # print(ret_dict_list[i]["groupContacts"])
        i += 1

    # return ret_dict_list


df = init_df()
append_df(get_test_dict1())
append_df(get_test_dict2())
append_df(get_test_dict3())
append_df(get_test_dict4())
append_df(get_test_dict5())
# test_df()
# print(df.sort_values('contactName', ascending=True).text.values)
print(df.contactName.unique())
latest_msgs_df = df.drop_duplicates(subset='contactName')
print(latest_msgs_df)




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