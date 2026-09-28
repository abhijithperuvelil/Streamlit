import streamlit as st
from library_db import BookListCreateRetrieveUpdateDelete

st.title("Update Book Record")
id=st.number_input("Enter the ID: ",min_value=0)
title=st.text_input("Enter the Title: ")
author=st.text_input("Enter the Author Name: ")
price=st.number_input("Enter the Price: ",min_value=0)
page=st.number_input("Enter the Pages: ",min_value=0)
language=st.text_input("Enter the Language: ")
btn=st.button("Submit")
if btn:
    b=BookListCreateRetrieveUpdateDelete()
    a=b.update(id,title,author,price,page,language)
    if a>0:
        st.success("Updated Successfully")
    else:
        st.error("No Id Found")
