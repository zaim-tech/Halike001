import streamlit as st
import time
import webbrowser

st.set_page_config(page_title="Halike Production", layout="centered")

# Initialize session state
if 'page' not in st.session_state:
    st.session_state.page = 'Home'

# Sidebar Navigation
st.sidebar.title('Navigation')
if st.sidebar.button('Order and messaging page'):
    st.session_state.page = 'OrderPage'

# Handle page switching
if st.session_state.page == 'OrderPage':
    import halike2  # This must be another file: halike2.py
else:
    # Main Home Page
    st.title('Halike Production')
    st.header('Welcome to Halike Production')
    st.image('halike.jpg', width=250, caption='halike production')

    name = st.text_input('**Enter your full name:**', placeholder='Enter full name')
    phone_no = st.text_input('**Enter your phone number:**', max_chars=10, placeholder='e.g. 0712345678')

    def zaim():
        with st.spinner('Wait to verify...'):
            time.sleep(2)
        st.success('Successfully verified.')
        st.write(f'**Hello, {name}, welcome to Halike Production!**')

    st.button('Verify Button', on_click=zaim)

    def yt():
        webbrowser.open('https://youtube.com/@halikeproduction4322?si=xi2fs90mFgGxLsbO')

    def ig():
        webbrowser.open('https://www.instagram.com/halike_production/')

    def fc():
        webbrowser.open('https://www.facebook.com/people/Halike-Production/100057331515391/?sk=about')

    st.write('*Talented Videographer, Female drone pilot, photography & content creator. ' \
             'For all your events coverage.*')

    col1, col2 = st.columns([1, 2])

    st.button('**Visit us on YouTube**', on_click=yt)

    with col1:
        st.button('**Instagram**', on_click=ig)

    with col2:
        st.button('**Facebook**', on_click=fc)
