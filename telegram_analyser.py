import streamlit as st 
from processor import busy_users,tel_get_stats, get_stats_graph, most_used_words,most_emoji_used
from processor import month_year_timeline, week_timeline, month_timeline,hourly_timeline


def tel_app(df, user, chat_type):


    #setting up the columns
    c1, c2 = st.columns(2)

    #displaying information
    c1.header('Chat Analysis From')
    c1.write(f"<h2 style = 'color: green'> {df['time'].iloc[0]} </h2>", 
                unsafe_allow_html=True)
    
    c2.header('Chat Analysis Till')
    c2.write(f"<h2 style = 'color: red'> {df['time'].iloc[-1]} </h2>", 
                unsafe_allow_html=True)

    st.write('---')
    
    st.write("""<h1 style = 'text-align:center; color:blue'> 
        OverAll Stats 
        </h1>""",
        unsafe_allow_html=True)

    c1, c2 = st.columns(2)

    #showing the overall stats
    table_html, table= tel_get_stats(df,user)

    c1.write(table_html, unsafe_allow_html=True)

    fig = get_stats_graph(table)
    c2.plotly_chart(fig)

    # Showing the month-year time line
    st.write('---')

    st.write("""<h1 style = 'text-align:center; color:blue'> 
        Month Year TimeLine
        </h1>""",
        unsafe_allow_html=True)
    
    fig_line_y, fig_bar_y = month_year_timeline(df, user)
    st.plotly_chart(fig_line_y)
    st.plotly_chart(fig_bar_y)






    # Showing the month time line
    st.write('---')

    st.write("""<h1 style = 'text-align:center; color:blue'> 
        Month TimeLine
        </h1>""",
        unsafe_allow_html=True)
    
    fig_line_m, fig_bar_m= month_timeline(df, user)
    st.plotly_chart(fig_line_m)
    st.plotly_chart(fig_bar_m)








    # Showing the week time line
    st.write('---')

    st.write("""<h1 style = 'text-align:center; color:blue'> 
        Week TimeLine
        </h1>""",
        unsafe_allow_html=True)
    
    fig_line_w, fig_bar_w= week_timeline(df, user)
    st.plotly_chart(fig_line_w)
    st.plotly_chart(fig_bar_w)
    

    # Showing the hourly time line
    st.write('---')

    st.write("""<h1 style = 'text-align:center; color:blue'> 
        Hourly TimeLine
        </h1>""",
        unsafe_allow_html=True)


    fig_heat, fig_line= hourly_timeline(df, user)
    st.plotly_chart(fig_heat)
    st.plotly_chart(fig_line)
    




    # showing the most busy users

    if user == 'OverAll':
        st.write('---')

        st.write("""<h1 style = 'text-align:center; color:blue'> 
        Busy Users
        </h1>""",
        unsafe_allow_html=True)

        cl1, cl2 = st.columns(2)

        fig, busy_table = busy_users(df)

        # plotting the Graph
        cl1.plotly_chart(fig)

        # creating the table

        cl2.dataframe(busy_table)

    
    # Showing most used words
    st.write('---')

    st.write("""<h1 style = 'text-align:center; color:blue'> 
        Most Used Words
        </h1>""",
        unsafe_allow_html=True)
    
    most_used_words_df, fig = most_used_words(df, user)

    c1, c2 = st.columns(2)

    c1.dataframe(most_used_words_df)
    c2.plotly_chart(fig)


    # showing most used emoji
    st.write('---')

    st.write("""<h1 style = 'text-align:center; color:blue'> 
        Most Used Emoji
        </h1>""",
        unsafe_allow_html=True)
    
    most_used_emoji_df,fig= most_emoji_used(df, user)

    c1, c2 = st.columns(2)

    c1.dataframe(most_used_emoji_df)
    c2.plotly_chart(fig)


    


