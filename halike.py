import streamlit as st
import time 
import webbrowser


st.spinner('In progress')
time.sleep(3)
phne = '254700047229'


file = 'halike2.py'
st.title('Halike Production')

     
st.header('**Welcome to Halike production**')
st.image('halike.jpg',width=250, caption='halike production')

name = st.text_input('**Enter your full name:**', placeholder='Enter full name', width=250)
phone = st.text_input('**Enter your phone number:**', placeholder="e.g. 0712345678", width=250, max_chars=10)
if not name and  not phone:
     st.error('**Enter your name and phone number please**')
if st.button('Verifry Button'):
    st.spinner()
    time.sleep(3)
    st.success('Successfully verifry')

st.write('Talented Videographer, Female drone pilot, photography & content creator. For all your events coverage.')

if st.button('**Click to make order or chat with halike**'):
     webbrowser.open(f'https://wa.me/{phne}')
msg = st.text_input('**Your message or order to Halike:**', placeholder='Your message or order')
if st.button('**Submit**'):
        
        message = f'Name: {name}, phone number: {phone}, my massage to Halike: {msg}'
        
        webbrowser.open(f'https://wa.me/{phne}?text={message}')
st.write('**Also reach as on:**')
col1, col2, col3 = st.columns([1,2,3])

with col1:
    if st.button('Youtube'):
        webbrowser.open('https://www.youtube.com/channel/UCnoegWJEEDp445IjeZT4fPg')

with col2:
    if st.button('Facebook'):
        webbrowser.open('https://www.facebook.com/p/Halike-Production-100057331515391/')

with col3:
    if st.button('Instagram'):
        webbrowser.open('https://www.instagram.com/reel/Cl_AreYDhJW/')
