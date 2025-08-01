import streamlit as st
import time 
import webbrowser


st.spinner('In progress')
time.sleep(3)
phne = '254722106055'


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

st.link_button('**Click to make order or chat with halike**', f'https://wa.me/{phne}')
     
msg = st.text_input('**Your message or order to Halike:**', placeholder='Your message or order')

        
message = f'Name: {name}, phone number: {phone}, my massage to Halike: {msg}'
st.link_button('**Submit**', f'https://wa.me/{phne}?text={message}') 

st.write('**Also reach as on:**')
col1, col2, col3 = st.columns([1,2,3])

with col1:
     st.link_button('Youtube', 'https://www.youtube.com/channel/UCnoegWJEEDp445IjeZT4fPg')
        

with col2:
     st.link_button('Facebook', 'https://www.facebook.com/p/Halike-Production-100057331515391/')
        

with col3:
    st.link_button('Instagram', 'https://www.instagram.com/reel/Cl_AreYDhJW/')
