import streamlit as st
from app import *

st.set_page_config(page_title="Database Q/A App", page_icon=":bookmark_tabs:")

st.image("logo.jpg",width=100)
st.title('Skillcurb Database :red[Q/A App] 	:open_book:')



question = st.text_input(":violet[Question: ]")
submit=st.button("Submit")

if question and submit:
    chain=get_db_chain()
    response=chain.run(question)
    st.header("Answer")
    st.write(response)