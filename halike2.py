import streamlit as st
import webbrowser

st.title('Halike Productions')

col1, col2 = st.columns([1, 2])
with col1:
    st.image('halike.jpg')

with col2:
    st.header('Welcome to Halike Production')


if 'show_form' not in st.session_state:
    st.session_state.show_form = False

def show_form():
    name = st.text_input('**Enter your full name:**', placeholder='Enter your full name')
    ph = st.text_input('**Enter phone number:**', placeholder='e.g. 700000000', max_chars=10)
    ms = st.text_input('**Enter your message or order and other issues:**', placeholder='Enter your message or order and other issues.')

    if st.button('Submit'):
        phone = '254700047229' 
        message = f'Name: {name}, phone: {ph}, message or order: {ms}'
        webbrowser.open(f'https://wa.me/{phone}?text={message}')
        st.success("Opening WhatsApp...")

def wtf():
    webbrowser.open('https://wa.me/254700047229')

col, col3 = st.columns([1, 2])
with col:
    if st.button('**Click to make order or message**'):
        st.session_state.show_form = True  

if st.session_state.show_form:
    show_form()

with col3:
    st.button('Click to chat with Halike about services', on_click=wtf)
