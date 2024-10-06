import pandas as pd
import re
import json

def create_dataframe(data):

    # making the pattern for 08/01/24,
    pattern = r'\d{1,2}/\d{1,2}/\d{2,4},'
    
    # creating list to store timestamp and messages
    timestamps = []
    messages = []


    # looping through messages to store timestamp and messages
    for message in data:

        # checking if the pattern is present in line
        if re.search(pattern, message):
            time, msg = message.split(' - ', maxsplit = 1)
            timestamps.append(time)
            messages.append(msg)

        # if pattern is not present , then it means that the line is 
        # extension of the previous message 
        else:
            messages[-1] = messages[-1]+message

    df = pd.DataFrame({'time':timestamps, 'chat':messages})

    # converting the date and time to proper format
    df['time'] = pd.to_datetime(df['time'], format = 'mixed')

    messages = []
    users = []

    # seperating the users and messages from the chat
    for message in df['chat']:

        # it splits the chat on user and the message by them
        entry = re.split('([\W\w]+?): ', message)

        if entry[1:]:
            users.append(entry[1])
            messages.append(entry[2])

        else:
            users.append('group notification')
            messages.append(entry[0])

    df['users'] = users
    df['messages'] = messages

    # creating a unique column for each date time
    df['year'] = df['time'].dt.year
    df['month'] = df['time'].dt.month_name()
    df['day'] = df['time'].dt.day
    df['hour'] = df['time'].dt.hour
    df['day_name'] = df['time'].dt.day_name()

    return df






def create_dataframe_json(data):

    data = json.load(data)

    #list to store data
    time = []
    users = []
    messages = []
    types = []

    # which type of chat it is

    chat_type = data['type']

    # iterating through the messages
    for msg in data['messages']:

        # if it is of notification type
        if msg['type'] == 'service':
            time.append(msg['date'])
            users.append('group notification')
            messages.append(msg['action'])
            types.append('service')

        # message or media chats
        else:
            time.append(msg['date'])
            if msg['from'] == None:
                users.append('deleted_users')
            else:
                users.append(msg['from'])

            # if the chat is media
            if ('file' in msg) or ('photo' in msg):

                # if the type of media is specified
                if 'mime_type' in msg:
                    types.append(msg['mime_type'])
                # else the type of media is not specified
                else:
                    types.append('media')

                # if there are messages associated with the media

                # if the media messages are multiple
                if isinstance(msg['text'], list):
                    mg = ''
                    for i in msg['text_entities']:
                        mg = mg + i['text'] + '\t'
                    messages.append(mg)
                
                # if media message is not specified add file name as media message
                elif (msg['text'] == '') and ('file_name' in msg):
                    messages.append(msg['file_name'])

                # id nothing is specified just add media
                else:
                    messages.append('media')

            # it is the messages sent and received
            else:
                types.append('message')

                # if multiple messages
                if isinstance(msg['text'], list):
                    mg = ''
                    for i in msg['text_entities']:
                        mg = mg + i['text'] + '\t'
                    messages.append(mg)
                else:
                    messages.append(msg['text'])

    df = pd.DataFrame({'time':time, 'users':users,
                   'type':types, 'messages':messages})
    
    df['time'] = pd.to_datetime(df['time'])
    
    df['year'] = df['time'].dt.year
    df['month'] = df['time'].dt.month_name()
    df['day'] = df['time'].dt.day
    df['hour'] = df['time'].dt.hour
    df['day_name'] = df['time'].dt.day_name()

    return chat_type, df