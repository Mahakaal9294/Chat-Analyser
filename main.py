import streamlit as st 
from preprocessor import create_dataframe, create_dataframe_json
import information
from whatsapp_analyser import wht_app
from telegram_analyser import tel_app

# Setting up the page
st.set_page_config(
    page_title='Chat Analyser',
    page_icon='bar_chart'
)

# Adding the sidebar
st.sidebar.write(""" 
        <h1 style = 'text-align:center; color:#0066FF'>
            CHAT ANALYSER
        </h1>
    """,
    unsafe_allow_html=True)

# creating a file uploader to upload file
uploaded_file = st.sidebar.file_uploader('Upload the file', 
                         accept_multiple_files=False,
                         type=['txt','json']
                         )

# if the file is not uploaded and show description
if uploaded_file is None:
    
    information.app()

else:
    
    # if the uploaded file is json file do telegram analysis
    if uploaded_file.name.endswith('.json'):
        st.write("""<h1 style = 'text-align:center; color:#0066FF'> 
                    TELEGRAM CHAT ANALYSER 
                </h1>""",
                unsafe_allow_html=True)
        
        chat_type , df = create_dataframe_json(uploaded_file)


    # Do whatapp analysis
    else:
        st.write("""<h1 style = 'text-align:center; color:#0066FF'> 
                WHATSAPP CHAT ANALYSER 
            </h1>""",
            unsafe_allow_html=True)
        
        # file received by streamlit is in byte mode
        # reading the file in byte mode
        bytes_data = uploaded_file.getvalue()

        # converting the file to string
        file = bytes_data.decode('utf-8')

        # creating a list of lines in the file
        file = file.split('\n') 
        df = create_dataframe(file)

    st.write('---')


    # getting the users list
    users_list = df['users'].unique().tolist()

    # removing group notification and adding overall 
    if 'group notification' in users_list:
        users_list.remove('group notification')
    if 'deleted_users' in users_list:
        users_list.remove('deleted_users')
    users_list.sort()
    users_list.insert(0,'OverAll')
    

    # storing the selected user
    selected_user = st.sidebar.selectbox('Show Analysis WRT', users_list)

    if st.sidebar.button('Show Analysis'):

        if uploaded_file.name.endswith('.json'):
            tel_app(df, selected_user, chat_type)

        else:
            wht_app(df,selected_user)
