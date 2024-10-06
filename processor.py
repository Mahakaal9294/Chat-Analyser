import emoji.unicode_codes
from urlextract import URLExtract
import plotly.express as px
import pandas as pd
from collections import Counter
import emoji



# object for urlExtract
url_extract = URLExtract()


#loading the stop_words
with open('stop_hinglish.txt','r') as f:
    stop_words = f.read()

###############################################################################################################################################

# to get the whatsapp stats
def wht_get_stats(df, user):

    # seletct the dataframe according to the user
    if user != 'OverAll':
        df = df[df['users'] == user]
    
    total_messages = df.shape[0]

    words = [word for i in df['messages'] for word in i.split()]
    words_len = len(words)

    media = df[df['messages'] == '<Media omitted>'].shape[0]

    urls = []
    for message in df['messages']:
        urls.extend(url_extract.find_urls(message) )
    ulrs_len = len(urls)

    table = pd.DataFrame({'Total Messages':total_messages,
                          'Total Words':words_len,
                            'Total Media':media,
                            'Total Links':ulrs_len},
                            index = ['Values'])

    table_html = table.T.to_html(escape=False).replace('<td>', '<td style="font-weight: bold;">')
    return table_html,table.T

###############################################################################################################################################

# to get the telegram stats
def tel_get_stats(df, user):
    
    if user != 'OverAll':
        df = df[df['users'] == user]
    
    total_messages = df.shape[0]

    words = [word for i in df['messages'] for word in i.split()]
    words_len = len(words)

    urls = []
    for message in df['messages']:
        urls.extend(url_extract.find_urls(message) )
    ulrs_len = len(urls)

    total_media = df[(df['type'] != 'service') & (df['type'] != 'message')].shape[0]

    total_video = df[df['type'].str.contains('video', case =False)].shape[0]
    total_image = df[df['type'].str.contains('image', case =False)].shape[0]
    total_documents = df[df['type'].str.contains('application', case =False)].shape[0]
    others = df[df['type'].str.contains('media', case =False)].shape[0]

    table = pd.DataFrame({'Total Messages':total_messages,
                          'Total Words':words_len,
                            'Total Media':total_media,
                            'Total Links':ulrs_len,
                            'Total Videos':total_video,
                            'Total Images':total_image,
                            'Total Documents':total_documents,
                            'Others':others
                          },
                          index = ['Values'])
    
    table_html = table.T.to_html(escape=False).replace('<td>', '<td style="font-weight: bold;">')
    return table_html,table.T


###############################################################################################################################################
def get_stats_graph(df):

    fig = px.bar(df, x=df.index, y='Values',
                 title='Stats Counts',
                labels = {'index' : 'Category', 'Values':'Count'})
    return fig
    
###############################################################################################################################################
def busy_users(df):

    busy_df = round(((df['users'].value_counts()/df.shape[0])*100),2).reset_index()
    busy_df.rename(columns={'users':'Users','count':'Percentage'}, inplace=True)

    fig = px.bar(busy_df, x="Users", y ="Percentage",
                 title='Busy Users',
                labels = {'name' : 'Users', 'y':'Count'})

    return fig, busy_df



###############################################################################################################################################
def most_used_words(df, user):

    if user != 'OverAll':
        df = df[df['users'] == user]

    columns = df.columns.tolist()

    # the dataframe should not contain media omitted and this edited
    df = df[~df['messages'].str.contains('<this|<Media', case =False)]

    if 'type' in columns:
        df = df[df['type'] == 'message']

    if 'group notification' in df['users'].unique().tolist():
        df = df[df['users'] != 'group notification']

    if 'deleted_users' in df['users'].unique().tolist():
        df = df[df['users'] != 'deleted_users']

    words = []

    for i in df['messages']:
        for word in i.lower().split():
            if word not in stop_words:
                words.append(word)

    most_word_df = pd.DataFrame(Counter(words).most_common(25), columns=['Word', 'Count'])


    fig = px.bar(most_word_df, x="Word", y ="Count",
                 title='Most Used Words')

    return most_word_df, fig

###############################################################################################################################################
def most_emoji_used(df, user):

    if user != 'OverAll':
        df = df[df['users'] == user]

    emojis = []

    for message in df['messages']:
        emoji_list = emoji.emoji_list(message)
        if emoji_list != []:
            emojis.extend([i['emoji'] for i in emoji_list])

    most_emoji_df = pd.DataFrame(Counter(emojis).most_common(25), columns=['Emoji', 'Count'])

    fig = px.bar(most_emoji_df, x="Emoji", y ="Count",
                 title='Most Used Words')

    return most_emoji_df,fig


###############################################################################################################################################
def month_year_timeline(df, user):

    if user != 'OverAll':
        df = df[df['users'] == user]

    timeline = df.groupby(['year','month']).count()['messages'].reset_index()

    month_year = []

    for i in range(timeline.shape[0]):
        month_year.append(timeline['month'][i] +'-' + str(timeline['year'][i]))

    timeline['month-year'] = month_year

    fig_line = px.line(timeline, x='month-year', y= 'messages',
                  title='Month- Year TimeLine')

    fig_bar = px.bar(timeline, x='month-year', y= 'messages',
                  title='Month- Year TimeLine')

    return fig_line, fig_bar

###############################################################################################################################################
def week_timeline(df, user):

    if user != 'OverAll':
        df = df[df['users'] == user]

    timeline = df.groupby(['day_name']).count()['messages'].reset_index()

    fig_line = px.line(timeline, x='day_name', y= 'messages',
                  title='Weekly TimeLine')
    
    fig_bar = px.bar(timeline, x='day_name', y= 'messages',
                  title='Weekly TimeLine')

    return fig_line, fig_bar

###############################################################################################################################################
def month_timeline(df, user):

    if user != 'OverAll':
        df = df[df['users'] == user]

    timeline = df.groupby(['month']).count()['messages'].reset_index()

    fig_line = px.line(timeline, x='month', y= 'messages',
                  title='Monthly TimeLine')
    

    fig_bar = px.bar(timeline, x='month', y= 'messages',
                  title='Monthly TimeLine')

    return fig_line, fig_bar

###############################################################################################################################################
def hourly_timeline(df,user):

    if user != 'OverAll':
        df = df[df['users'] == user]

    df['period'] = df['hour'].astype(str) + ':' + (df['hour'] + 1).astype(str)

    # Handle the case when hour is 23, which should roll over to '23-0'
    df.loc[df['hour'] == 23, 'period'] = '23-0' 

    hourly_df = df.pivot_table(index = 'day_name', columns = 'period', values='messages',
                   aggfunc= 'count').fillna(0).reset_index()
    
    columns = hourly_df.columns[1:].values
    rows = hourly_df['day_name'].values

    t = hourly_df.iloc[:,1:].values

    fig_heat = px.imshow(t,
                    labels=dict(x='Time Period', y='Day Name', color='Number of Messages'),
                    x=columns,
                    text_auto=True,
                    aspect='auto',
                    color_continuous_scale='RdBu_r',
                    y=rows)


    df_melt = hourly_df.melt(id_vars='day_name', var_name='time', value_name='num_msg')

    # Create the multi-line graph
    fig_line = px.line(
        df_melt,
        x='time',
        y='num_msg',
        color='day_name',  # Plot lines by day_name
        title='Messages Over Different Time Periods',
        labels={
            'time': 'Time Period',
            'num_msg': 'Number of Messages',
            'day_name': 'Day of the Week'
        }
    )



    return fig_heat, fig_line