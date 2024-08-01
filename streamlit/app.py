import streamlit as st
from datetime import datetime
from Functions.auth_functions import login_user, register_user
from Functions.db_functions import log_data, user_data
from openaiApi import OpenAIAPI
from decouple import config
from PIL import Image


st.set_page_config(page_title="RetainAI", page_icon=None, layout="centered", initial_sidebar_state="auto", menu_items=None)
with st.sidebar:
    # options menu  
    selected = st.selectbox("Menu", ['Sign Up',"Log In"])
    
    # log in form
    if 'login' not in st.session_state:
        st.session_state['login'] = False

   


    if selected == "Log In":
        
        st.write('## Log In')
        if 'username' in st.session_state and st.session_state['username'] != None: 
            login_username = st.session_state['username']
        else:
            login_username = st.text_input('Email')
        login_password = st.text_input('Password', type='password')
        # authentication status update
        if st.button('Log In!'):
            # send login request 
            st.session_state['login'] = login_user(login_username,login_password)

        if st.session_state['login'] == True:
            st.session_state['username'] = login_username
            if st.button("Logout"):
                st.session_state['login'] = False
                st.session_state['username'] = None
                

    # # Sign-up form 
    if selected == "Sign Up":
        st.write('## Sign up')
        name = st.text_input('Name')
        username = st.text_input('Email',key='signup_username')
        plan = st.selectbox(
                    "Select Plan",
                ["free", "gold","platinum"]
                )

        password = st.text_input('Password', type='password',key='signup_pass')
        confirm_password = st.text_input('Confirm Password', type='password')

        
        if st.button('Sign up'):
            if password != confirm_password:
                st.write("Passwords don't Match!")
            else:
                # send register request 
                signup_status = register_user(name,username,password,plan)
                if signup_status:
                    st.success("User Registered Successfully! Sign-in to continue...")
                else:
                    st.error("Email already exists! Sign in to continue...")

if  st.session_state['login'] != True:
    st.title("Welcome to Retain.ai")
    st.subheader("retain your thoughts that you always keep forgetting!")
    st.write("sign-up and log-in to use. This will let you revisit your messages in the future!!")
    st.write("how get your open_ai keys: https://www.howtogeek.com/885918/how-to-get-an-openai-api-key/ ")
    st.title("⬅ ⬅ Sign-up now!!")
    image = Image.open('streamlit/database/alterok.png')
    st.image(image)
    
if  st.session_state['login'] == True:

    st.title("Welcome to the Chatbox")
    openai_key = st.text_input("Enter your open_ai key")
    openai_requests = OpenAIAPI(openai_key)

    with st.form("my_form"):
        message = st.text_area("Type message to remember")
        submit = st.form_submit_button("Send")

    if submit:
        log_data(st.session_state['username'], datetime.now(),message)


   

    df = user_data(st.session_state['username'])
    df = df.drop(columns="username")
    st.dataframe(data=df,use_container_width=True)
    df_dict = df.to_dict(orient='records')
    context_str = str(df_dict)
    st.write("## Sumarize the Data")
    if st.button("Summarize"):
            summarize = openai_requests.request_summarization(context_str)
            st.write(summarize)

    
    st.write("## Organize the Data")
    if st.button("Organize"):
            organize = openai_requests.request_organization(context_str)
            st.write(organize)

    st.write("## Search in the Data")
    search = st.text_input("Search through data")
    if st.button("Search"):
            search_res = openai_requests.request_search(f"{context_str} /n use the context to answer {search}")
            st.write(search_res)


    