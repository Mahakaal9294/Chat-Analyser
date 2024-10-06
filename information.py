import streamlit as st 

def app():

    st.write("""<h1 style = 'text-align:center; color:#0066FF'> 
            Chat Analyzer for WhatsApp and Telegram 
             </h1>""",
            unsafe_allow_html=True)
    st.write('---')

    st.write("""
                <h2 style ='text-align:center; color:green' >
                    Overview
                </h2>
                """,
                unsafe_allow_html=True)

    st.write("""
                <p style ='text-align:center; justify-content: center;' >
                    The Chat Analyzer is a powerful tool designed to provide in-depth 
                    insights into your messaging patterns and communication dynamics on
                    WhatsApp and Telegram. By analyzing chat data, users can gain valuable
                    information about sentiment, engagement, and conversation topics. 
                    This tool distinguishes between the two platforms based on the file 
                    type you upload: JSON files for Telegram chats and text files for 
                    WhatsApp chats.
                    </p>
                """,    
                unsafe_allow_html=True)
    
    st.write('---')

    st.write("""
                <h2 style ='text-align:center; color:green' >
                    How It Works
                </h2>
                """,
                unsafe_allow_html=True)
    
    st.write("""
            <h3> 
                1.File Upload Instructions:
            </h3>
            """,
            unsafe_allow_html=True)
    
    st.write("""
                <ul>
                    <li>   
                        <p style ='justify-content: space-between;'>
                            <h4>Telegram Chats: </h4>If you want to analyze your Telegram chat, 
                            please upload a JSON file. You can export your Telegram 
                            chats directly from the app in this format.
                        </p>
                    </li>
                    <li>   
                        <p style ='justify-content: space-between;'>
                            <h4>WhatsApp Chats: </h4> To analyze your WhatsApp conversations, 
                            lease upload a plain text (.txt) file. You can export your chats by selecting the 
                            chat in WhatsApp, then choosing the "Export Chat" option.
                        </p>
                    </li>
            </ul>
            """,
            unsafe_allow_html=True)


    st.write("""
            <h3> 
                2. Data Analysis Process
            </h3>
            """,
            unsafe_allow_html=True)
    
    st.write("""
                <ul>
                    <li>   
                        <p style ='justify-content: space-between;'>
                            Once you've uploaded the correct file type, our Chat 
                            Analyzer will automatically detect the format and begin the analysis.
                        </p>
                    </li>
                    <li>   
                        <p style ='justify-content: space-between;'>
                            The tool processes the data to extract meaningful insights, 
                            including sentiment analysis, engagement metrics, and keyword trends.
                        </p>
                    </li>
            </ul>
            """,
            unsafe_allow_html=True)
    
    st.write('---')


    st.write("""
                <h2 style ='text-align:center; color:green' >
                    Key Features
                </h2>
                """,
                unsafe_allow_html=True)
    

    st.write("""
                <ul>
                    <li>   
                        <p style ='justify-content: space-between;'>
                            <h4>Engagement Metrics:</h4>
                            Analyze message frequency, response times,
                            and identify the most active participants in your conversations. 
                            Discover engagement trends to improve communication dynamics.
                        </p>
                    </li>
                    <li>   
                        <p style ='justify-content: space-between;'>
                            <h4>Keyword and Topic Analysis</h4>Identify frequently used words 
                            and phrases, uncovering the primary subjects of discussion. This 
                            feature helps highlight common themes in your chats.
                        </p>
                    </li>
                    <li>   
                        <p style ='justify-content: space-between;'>
                            <h4>Visualizations</h4>View dynamic charts and graphs that illustrate 
                            communication patterns and sentiment trends. Easily interpret your 
                            data with visual aids.
                        </p>
                    </li>
                    <li>   
                        <p style ='justify-content: space-between;'>
                            <h4>Exportable Reports</h4>Generate detailed reports of your chat 
                            analysis that can be exported in PDF or Excel formats for sharing 
                            with others or for personal records.
                        </p>
                    </li>
                    <li>   
                        <p style ='justify-content: space-between;'>
                            <h4>Privacy and Security</h4>Your privacy is paramount. The tool 
                            ensures that all data is handled securely and complies with data protection regulations. Options for anonymization are available to protect sensitive information.
                        </p>
                    </li>
            </ul>
            """,
            unsafe_allow_html=True)
    
    st.write('---')

    st.write("""
                <h2 style ='text-align:center; color:green' >
                    User Guidelines
                </h2>
                """,
                unsafe_allow_html=True)
    
    st.write("""
                <ul>
                    <li>   
                        <p style ='justify-content: space-between;'>
                            Please ensure that you upload your files in the correct format to avoid any processing errors:
                        </p>
                    </li>
                    <li>   
                        <p style ='justify-content: space-between;'>
                            <b>Telegram Chat: </b>
                            Upload a JSON file.
                        </p>
                    </li>
                    <li>   
                        <p style ='justify-content: space-between;'>
                            <b>WhatsApp Chat:  </b>
                            Upload a text (.txt) file.
                        </p>
                    </li>
                    <li>   
                        <p style ='justify-content: space-between;'>
                            If the file format is incorrect, the analysis will not proceed, and you will be prompted to upload a compatible file.
                        </p>
                    </li>
            </ul>
            """,
            unsafe_allow_html=True)